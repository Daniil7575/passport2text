import sqlite3
import os


class DB:
    def __init__(self) -> None:
        directory = os.getcwd()
        print(directory)
        self.db = sqlite3.connect('pass2text/db.db')
        self.cursor = self.db.cursor()
        self.init_db()
    
    def init_db(self):
        try:
            self.cursor.execute("""
                    CREATE TABLE "person" (
                        "series" INTEGER,
                        "number" INTEGER,
                        "surname" TEXT,
                        "name" TEXT,
                        "patronymic" TEXT,
                        "gender" TEXT,
                        "birth_date" TEXT,
                        "birth_place" TEXT,
                        "issue_date" TEXT,
                        "issue_place" TEXT,
                        "code" TEXT,
                        PRIMARY KEY("series","number")
                    );
                """)

            self.db.commit()
        except sqlite3.OperationalError:
            pass
