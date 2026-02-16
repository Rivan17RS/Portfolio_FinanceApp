from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QComboBox,
    QLineEdit, QDateEdit, QMessageBox, QTableWidget,
    QTableWidgetItem, QHeaderView
)
from PyQt6.QtCore import QDate
from database import fetch_expenses, add_expenses, delete_expenses
from styles import get_stylesheet



class ExpenseApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle("Expense Tracker")

        self.layout = QVBoxLayout()

        # Inputs
        self.date_label = QLabel("Date:")
        self.date_input = QDateEdit()
        self.date_input.setCalendarPopup(True)
        self.date_input.setDate(QDate.currentDate())

        self.category_label = QLabel("Category:")
        self.category_input = QComboBox()
        self.category_input.addItems([
            "Fast Food", "Groceries", "Transport", "Utilities",
            "Entertainment", "Medical Expenses", "Loans", "Rent", "Other"
        ])

        self.amount_label = QLabel("Amount:")
        self.amount_input = QLineEdit()

        self.description_label = QLabel("Description:")
        self.description_input = QLineEdit()

        self.add_button = QPushButton("Add Expense")
        self.add_button.clicked.connect(self.add_expense)
        self.add_button.setObjectName("addButton")

        self.delete_button = QPushButton("Delete Selected Expense")
        self.delete_button.clicked.connect(self.delete_expense)
        self.delete_button.setObjectName("deleteButton")

        # Table
        self.expense_table = QTableWidget()
        self.expense_table.setColumnCount(5)
        self.expense_table.setHorizontalHeaderLabels(
            ["ID", "Date", "Category", "Amount", "Description"]
        )
        self.expense_table.setColumnHidden(0, True)
        self.expense_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )
        self.expense_table.setSelectionBehavior(
            QTableWidget.SelectionBehavior.SelectRows
        )
        self.expense_table.setSelectionMode(
            QTableWidget.SelectionMode.SingleSelection
        )
        self.expense_table.setMouseTracking(True)

        # Layout
        self.layout.addWidget(self.date_label)
        self.layout.addWidget(self.date_input)
        self.layout.addWidget(self.category_label)
        self.layout.addWidget(self.category_input)
        self.layout.addWidget(self.amount_label)
        self.layout.addWidget(self.amount_input)
        self.layout.addWidget(self.description_label)
        self.layout.addWidget(self.description_input)
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.delete_button)
        self.layout.addWidget(self.expense_table)

        self.setLayout(self.layout)

        # ✅ LOAD DATA ON STARTUP
        self.load_expenses()

    # ------------------------
    # Add Expense
    # ------------------------
    def add_expense(self):
        date = self.date_input.date().toString("yyyy-MM-dd")
        category = self.category_input.currentText()
        amount = self.amount_input.text()
        description = self.description_input.text()

        if not amount or not amount.replace('.', '', 1).isdigit():
            QMessageBox.warning(self, "Input Error", "Please enter a valid amount.")
            return

        if not description.strip():
            QMessageBox.warning(self, "Input Error", "Please enter a description.")
            return

        if add_expenses(date, category, float(amount), description):
            self.load_expenses()
            self.clear_inputs()
        else:
            QMessageBox.critical(self, "Error", "Failed to add expense.")

    # ------------------------
    # Delete Expense
    # ------------------------
    def delete_expense(self):
        selected_row = self.expense_table.currentRow()

        if selected_row == -1:
            QMessageBox.warning(self, "Selection Error", "Please select an expense.")
            return

        reply = QMessageBox.question(
            self,
            "Delete Expense",
            "Are you sure you want to delete this expense?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply != QMessageBox.StandardButton.Yes:
            return

        expense_id = int(self.expense_table.item(selected_row, 0).text())

        if delete_expenses(expense_id):
            self.load_expenses()
        else:
            QMessageBox.critical(self, "Error", "Failed to delete expense.")

    # ------------------------
    # Load Expenses
    # ------------------------
    def load_expenses(self):
        expenses = fetch_expenses()
        self.expense_table.setRowCount(0)

        for expense in expenses:
            row = self.expense_table.rowCount()
            self.expense_table.insertRow(row)

            for col in range(5):
                self.expense_table.setItem(
                    row, col, QTableWidgetItem(str(expense[col]))
                )

    # ------------------------
    # Clear Inputs
    # ------------------------
    def clear_inputs(self):
        self.amount_input.clear()
        self.description_input.clear()
        self.date_input.setDate(QDate.currentDate())
        self.category_input.setCurrentIndex(0)

