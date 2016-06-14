from __future__ import print_function

import pymysql


class MySQLConnector:
    host = ''
    port = 0
    login = ''
    password = ''
    db = ''

    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 3306
        self.login = 'root'
        self.password = 'root'
        self.db = 'predictor'

    def insert_item(self, date, teama, teamb, preda, predx, predb):
        conn = pymysql.connect(host=self.host,
                               port=self.port,
                               user=self.login,
                               passwd=self.password,
                               db=self.db,
                               autocommit=True)
        cur = conn.cursor()
        cur.execute("INSERT INTO `matches` VALUES ('" + str(date) + "', '" +
                    str(teama) + "', '" +
                    str(teamb) + "', '" +
                    str(preda) + "', '" +
                    str(predx) + "', '" +
                    str(predb) + "')")
        cur.close()
        conn.close()
        self.see_db()

    def see_db(self):
        conn = pymysql.connect(host=self.host,
                               port=self.port,
                               user=self.login,
                               passwd=self.password,
                               db=self.db,
                               autocommit=True)
        cur = conn.cursor()
        cur.execute("SELECT * FROM `matches`")
        print(cur.description)
        for row in cur:
            print(row)
        cur.close()
        conn.close()
