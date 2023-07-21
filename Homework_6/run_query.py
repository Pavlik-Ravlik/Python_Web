import sqlite3

QUERY_DICT = {
    '1': 'query_1.sql', 
    '2': 'query_2.sql', 
    '3': 'query_3.sql', 
    '4': 'query_4.sql', 
    '5': 'query_5.sql', 
    '6': 'query_6.sql', 
    '7': 'query_7.sql', 
    '8': 'query_8.sql', 
    '9': 'query_9.sql', 
    '10': 'query_10.sql',

}


def run():
    input_query_file = input('1 - Найти 5 студентов с наибольшим средним баллом по всем предметам.\n2 - Найти студента с наивысшим средним баллом по определенному предмету.\n3 - Найти средний балл в группах по определенному предмету.\n4 - Найти средний балл на потоке (по всей таблице оценок).\n5 - Найти какие курсы читает определенный преподаватель.\n6 - Найти список студентов в определенной группе.\n7 - Найти оценки студентов в отдельной группе по определенному предмету.\n8 - Найти средний балл, который ставит определенный преподаватель по своим предметам.\n9 - Найти список курсов, которые посещает определенный студент.\n10 - Список курсов, которые определенному студенту читает определенный преподаватель.\n>>>>>   ')
    
    with sqlite3.connect('salary.db') as conn:
        cursor = conn.cursor()

        for number, query_file in QUERY_DICT.items():
            if input_query_file == number:
                number_query = query_file

        with open(number_query, 'r') as file:
            query = file.read()
            cursor.execute(query)
            result = cursor.fetchall()
            print(result)




if __name__ == '__main__':
    run()
