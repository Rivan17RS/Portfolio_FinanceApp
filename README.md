💰 Desktop Finance App

A lightweight Personal Finance Manager built in Python that allows users to track income, expenses, and balances locally.

This project demonstrates:

* Clean application structure
* Local data persistence
* Simple financial tracking logic
* Version control best practices

NOTE: Expandability to a Flask web deployment is currently in progress (cloud-ready version).

🚀 Features

+ Add income
+ Add expenses
+ View transaction history
+ Calculate current balance
+ Local data storage
+ Simple and intuitive UI
+ Modular Python structure

🛠 Tech Stack

* Python 3
* (Tkinter / Custom UI library — adjust to what you're using)
* JSON / SQLite (adjust if needed)
* Git + GitHub

📂 Project Structure
finance-app/
│
├── main.py
├── app.py
├── database.py
├── styles.py
├── expense.db
└── README.md

🖥️ How to Run Locally
1️⃣ Clone the repository
```
git clone https://github.com/yourusername/finance-app.git
cd finance-app
```
2️⃣ Create virtual environment (recommended)

```
python -m venv venv
```

Activate it:

Windows
```
venv\Scripts\activate
```

Mac/Linux
```
source venv/bin/activate
```
3️⃣ Install dependencies
```
pip install -r requirements.txt
```
4️⃣ Run the app
```
python main.py
```
🌐 Cloud Version (Flask Deployment)

A web-based version of this project is coming soon, built using:

* Flask
* Render (deployment)
* Gunicorn
* Production-ready configuration

This demonstrates full-stack deployment capability and DevOps knowledge.

🎯 Purpose of This Project

This project was created for:

+ Portfolio demonstration
+ Showcasing Python fundamentals
+ Demonstrating software structure best practices
+ Showing evolution from desktop → cloud architecture
+ Highlighting DevOps mindset (environment setup, deployment-ready design)

📈 Future Improvements

* Authentication system
* Database migration to PostgreSQL
* Docker containerization
* CI/CD pipeline
* Expense categorization with analytics dashboard
* API endpoints for mobile integration

🏗 Architecture Evolution

This project is intentionally structured to demonstrate evolution:

* Desktop local application
* Refactored into Flask web app
* Cloud deployment (Render)
* Future: Docker + CI/CD
* This reflects real-world modernization patterns used in production systems.

👨‍💻 Author

Ivan Rojas Salazar
DevOps / SRE Engineer
Costa Rica 🇨🇷
License: MIT License
