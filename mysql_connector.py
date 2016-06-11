



class MySQLConnector:
    connection = None

    @staticmethod
    def connect_dbs():
        conn = pymysql.connect(host='localhost', port='3360', user='root', passwd='root', db='predictor')
        cur.execute("INSERT INTO matches VALUES ('', '', '', '"+date+"', '"+teama+"', '"+teamb+"', '"+preda+"', '"+predx+"', '"+predb+"' )")
        return conn

    def insert_item(self, date, teama, teamb, preda, predx, predb):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO matches VALUES ('', '', '', '"+date+"', '"+teama+"', '"+teamb+"', '"+preda+"', '"+predx+"', '"+predb+"' )")
        self.cur.close()
        self.conn.close()

    @staticmethod
    def get_items():
        cur = MySQLConnector.conn.cursor()
        cur.execute("SELECT * FROM matches")
        print(MySQLConnector.cur.description)
        print()
        for row in cur:
            print(row)
        MySQLConnector.cur.close()
        MySQLConnector.conn.close()

