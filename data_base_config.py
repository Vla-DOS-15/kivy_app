import pyodbc

class database_config:
    # Параметри підключення до бази даних
    server = '(localdb)\\mssqllocaldb'
    database = 'AccountingOfFamilyFinancesDB'

    # Строка підключення
    connection_string = f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};'

    # Встановлення з'єднання з базою даних
    conn = pyodbc.connect(connection_string)

    # Створення курсора
    cursor = conn.cursor()

    # Виконання SQL-запиту
    cursor.execute('SELECT * FROM Users')

    # Отримання результатів запиту
    for row in cursor:
        print(row)

    # Закриття курсора та з'єднання
    cursor.close()
    conn.close()
