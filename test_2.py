import pymysql

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

    # Insert query
    insert_query = "INSERT INTO Users (FIRSTNAME, LASTNAME, EMAIL, JOB_PREFERENCES, PROFESSIONAL_DOMAIN, PASSWORD) VALUES (%s, %s, %s, %s, %s, %s);"

    # Values to insert
    values = ('Justice', 'Chukwuonye', 'j.chukwuony@alustudent.com', 'Cyber security', 'Technology (Tech)', 'Justice123')

    # Execute the insert query
    cursor.execute(insert_query, values)

    # Commit the changes
    connection.commit()

    print("User inserted successfully!")

    # Don't forget to close the cursor and connection when you're done
    cursor.close()
    connection.close()

except pymysql.Error as err:
    print("Error:", err)