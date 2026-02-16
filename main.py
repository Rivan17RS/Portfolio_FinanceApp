# running the app (pyqt6 installed)
import sys
from PyQt6.QtWidgets import QApplication, QMessageBox
from database import init_db
from app import ExpenseApp
from styles import get_stylesheet



def main():
    app = QApplication(sys.argv)

    app.setStyleSheet(get_stylesheet())

    if not init_db("expense.db"):
        QMessageBox.critical(None, "Error!", "Failed to load the database.")
        sys.exit(1)

    window = ExpenseApp()
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
