import sqlite3


# Return results of query
def query(query, type):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute(query)
    if type == 'select':
        results = cursor.fetchall()
        return results
    elif type == 'insert':
        connection.commit()
    else:
        pass
    connection.close()


# Initialize database
if __name__ == "__main__":
    connection = sqlite3.connect('database.db')
    print('Opened database successfully')

    connection.execute('CREATE TABLE if not exists foods (name TEXT, calories TEXT, cuisine TEXT, is_vegetarian TEXT, is_gluten_free TEXT)')
    print('Table created successfully')

    connection.close()
