try:
    import sqlite3

    connect = sqlite3.connect('db.sqlite3')
    cursor = connect.cursor()
    cursor.execute('DROP TABLE unic')
    cursor.close()
    connect.commit()

except sqlite3.Error as error:
    print("Некая непонятка", error)

finally:
    print("Я здесь")
