import pymysql


def search_user(email="", domain="", table=""):
    try:
        connection = pymysql.connect(
            host="sql8.freesqldatabase.com",
            port=3306,
            user="sql8639996",
            passwd="TVwDvwZI8t",
            database="sql8639996"
        )
        
        results = ()
        
        if table == "Users":

            query = "SELECT * FROM Users WHERE EMAIL = %s;"

            with connection.cursor() as cursor:
                cursor.execute(query, (email,))
                results = cursor.fetchall()
        
        if table == "Mentors":
            query = "SELECT * FROM Mentors WHERE PROFESSIONAL_DOMAIN = %s;"
            
            with connection.cursor() as cursor:
                cursor.execute(query, (domain,))
                results = cursor.fetchall()            


    except pymysql.Error as err:
        print("Database Error:", err)
        
    else:
        return results
        
    finally:
        connection.close()


if __name__ == "__main__":
    search_user('j.chukwuony@alustudent.com')