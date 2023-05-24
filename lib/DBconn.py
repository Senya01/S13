import pymysql
from config import host, user, password, db_name


def con(debug=False):
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        if debug:
            print('Successfully connected...')
            print("#" * 20)
        return connection

    except Exception as ex:
        print('Connection refused...')
        print(ex)
