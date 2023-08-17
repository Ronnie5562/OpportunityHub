import pymysql


def save_to_db(firstname, lastname, email, job_preference, my_domain, password="", exp_level="", table=""):
    try:
        # Connect to the database
        connection = pymysql.connect(
            host="sql8.freesqldatabase.com",
            port=3306,
            user="sql8639996",
            passwd="TVwDvwZI8t",
            database="sql8639996"
        )

        # Create a cursor object
        cursor = connection.cursor()
        
        
        if table == "Users":
            # Insert query
            insert_query = "INSERT INTO Users (FIRSTNAME, LASTNAME, EMAIL, JOB_PREFERENCES, PROFESSIONAL_DOMAIN, PASSWORD) VALUES (%s, %s, %s, %s, %s, %s);"

            # Values to insert
            values = (firstname, lastname, email, job_preference, my_domain, password)
            
            # Execute the insert query
            cursor.execute(insert_query, values)

            # Commit the changes
            connection.commit()

            print("""
                  Registration is successful !!!
                """)

            # Don't forget to close the cursor and connection when you're done
            cursor.close()
            connection.close()
        
        if table == "Mentors":
            # Insert query
            insert_query = "INSERT INTO Mentors (FIRSTNAME, LASTNAME, EMAIL, JOB_PREFERENCES, EXPERIENCE_LEVEL, PROFESSIONAL_DOMAIN) VALUES (%s, %s, %s, %s, %s, %s);"

            # Values to insert
            values = (firstname, lastname, email, job_preference, exp_level, my_domain)

            # Execute the insert query
            cursor.execute(insert_query, values)

            # Commit the changes
            connection.commit()

            print("""
                  You are now a mentor at OpportunityHub !!!
                """)

            # Don't forget to close the cursor and connection when you're done
            cursor.close()
            connection.close()

    except pymysql.Error as err:
        print("Error:", err)


if __name__ == "__main__":
    pass