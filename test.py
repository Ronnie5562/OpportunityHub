import pymysql


def search_user(email, password=None):
    try:
        connection = pymysql.connect(
            host="sql8.freesqldatabase.com",
            port=3306,
            user="sql8639996",
            passwd="TVwDvwZI8t",
            database="sql8639996"
        )

        query = "SELECT * FROM Users WHERE EMAIL = %s;"

        with connection.cursor() as cursor:
            cursor.execute(query, (email,))
            results = cursor.fetchall()

        print(results)  # Do something more meaningful with the results

    except pymysql.Error as err:
        print("Database Error:", err)
    finally:
        connection.close()


if __name__ == "__main__":
    search_user('j.chukwuony@alustudent.com')
