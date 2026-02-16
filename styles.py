# styles.py

def get_stylesheet():
    return """
    QWidget {
        background-color: #f5f7fa;
        font-family: 'Segoe UI';
        font-size: 14px;
        color: #1f2937;
    }

    QLabel {
        font-weight: 500;
        margin-top: 6px;
    }

    QLineEdit, QDateEdit, QComboBox {
        background-color: white;
        border: 1px solid #e5e7eb;
        border-radius: 12px;
        padding: 6px 10px;
        min-height: 30px;
    }

    QLineEdit:focus, QDateEdit:focus, QComboBox:focus {
        border: 2px solid #22c55e;
    }

    QPushButton {
        border-radius: 14px;
        padding: 8px 16px;
        font-weight: 600;
        min-height: 36px;
        border: none;
    }

    /* Add Button */
    QPushButton#addButton {
        background-color: #22c55e;
        color: white;
    }

    QPushButton#addButton:hover {
        background-color: #16a34a;
    }

    QPushButton#addButton:pressed {
        background-color: #15803d;
    }

    /* Delete Button */
    QPushButton#deleteButton {
        background-color: #ef4444;
        color: white;
    }

    QPushButton#deleteButton:hover {
        background-color: #dc2626;
    }

    QPushButton#deleteButton:pressed {
        background-color: #b91c1c;
    }

    /* Table */
    QTableWidget {
        background-color: white;
        border: none;
        border-radius: 16px;
        gridline-color: #f1f5f9;
    }

    QTableWidget::item {
        padding: 10px;
    }

    /* Hover entire row */
    QTableWidget::item:hover {
        background-color: #f0fdf4;
    }

    /* Selected row (active window) */
    QTableWidget::item:selected {
        background-color: #22c55e;
        color: white;
    }

    /* Selected row (window unfocused) */
    QTableWidget::item:selected:!active {
        background-color: #bbf7d0;
        color: #065f46;
    }

    QHeaderView::section {
        background-color: #eef2f7;
        border: none;
        padding: 10px;
        font-weight: 600;
    }

    QScrollBar:vertical {
        border: none;
        background: #f3f4f6;
        width: 8px;
        margin: 4px;
        border-radius: 4px;
    }

    QScrollBar::handle:vertical {
        background: #cbd5e1;
        border-radius: 4px;
    }

    QScrollBar::handle:vertical:hover {
        background: #94a3b8;
    }
    """
