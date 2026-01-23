# All SQL queries and database connection functions
from PyQt6.QtSql import QSqlDatabase, QSqlQuery

def init_db(db_name):
    database = QSqlDatabase.addDatabase("QSQLITE")
    database.setDatabaseName(db_name)
    
    if not database.open():
        return False
    
    query = QSqlQuery()
    query.exec(
        """
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            description TEXT
        )
        """
    )
    return True