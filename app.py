# App design and layout space
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QComboBox, QLineEdit, QDateEdit, QMessageBox, QTableWidget, QVBoxLayout, QTableWidgetItem, QHeaderView
from PyQt6.QtCore import Qt, QDate

class ExpenseApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Expense Tracker")  
        self.setGeometry(100, 100, 600, 400)
        self.layout = QVBoxLayout()

        # Input Design  
        self.date_label = QLabel("Date:")
        self.date_input = QDateEdit()
        self.date_input.setCalendarPopup(True)
        self.date_input.setDate(QDate.currentDate())

        self.category_label = QLabel("Category:")
        self.category_input = QComboBox()
        self.category_input.addItems(["Food", "Transport", "Utilities", "Entertainment", "Other"])

        self.amount_label = QLabel("Amount:")
        self.amount_input = QLineEdit()

        self.add_button = QPushButton("Add Expense")
        self.add_button.clicked.connect(self.add_expense)

        # Expense table
        self.expense_table = QTableWidget()
        self.expense_table.setColumnCount(3)
        self.expense_table.setHorizontalHeaderLabels(["Date", "Category", "Amount"])
        self.expense_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        # Adding widgets to layout
        self.layout.addWidget(self.date_label)
        self.layout.addWidget(self.date_input)
        self.layout.addWidget(self.category_label)
        self.layout.addWidget(self.category_input)
        self.layout.addWidget(self.amount_label)
        self.layout.addWidget(self.amount_input)
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.expense_table)

        self.setLayout(self.layout)

    def add_expense(self):
        date = self.date_input.date().toString("yyyy-MM-dd")
        category = self.category_input.currentText()
        amount = self.amount_input.text()

        if not amount or not amount.replace('.', '', 1).isdigit():
            QMessageBox.warning(self, "Input Error", "Please enter a valid amount.")
            return

        row_position = self.expense_table.rowCount()
        self.expense_table.insertRow(row_position)
        self.expense_table.setItem(row_position, 0, QTableWidgetItem(date))
        self.expense_table.setItem(row_position, 1, QTableWidgetItem(category))
        self.expense_table.setItem(row_position, 2, QTableWidgetItem(amount))

        # Clear input fields
        self.amount_input.clear()