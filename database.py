from os import stat
from config import DB
import pymysql


class Session:
    conn: any
    cursor: any
    cache: any
    exp: str

    def __init__(self):
        self.conn = pymysql.connect(
            host=DB["host"],
            user=DB["user"],
            password=DB["password"],
            db=DB["database"],
            port=DB["port"],
            charset="utf8",
        )
        self.cursor = self.conn.cursor()

    def execute(self, sql: str):
        self.cursor.execute(sql)
        self.cache = self.cursor.fetchall()
        self.conn.commit()
        return self.cache
