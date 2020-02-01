import MySQLdb

class Connection:
    def __init__(self):
        self.host = "remotemysql.com"
        self.database = "FN9HPlCnS4"
        self.user = "FN9HPlCnS4"
        self.passwd = "7JvI9lqKdJ"
        self.connection = MySQLdb.connect(host=self.host, user=self.user, passwd=self.passwd, database=self.database)
        self.cursor = self.connection.cursor()