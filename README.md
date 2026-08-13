# 🏦 ATM System — Python

A command-line ATM system built with **Python**, providing essential banking operations through an interactive terminal-based interface.

The system provides account authentication and core ATM operations such as balance inquiry, cash withdrawal, deposits, and transaction handling through a structured object-oriented design.

---

## ✨ Features

* 🔐 PIN-based account authentication
* 💰 Balance inquiry
* 💸 Cash withdrawal
* 💵 Cash deposit
* 🏦 Account management
* 📋 Transaction handling
* ⚠️ Input validation
* 🔒 Authentication and transaction flow
* 🖥️ Interactive command-line interface
* 🧩 Object-oriented application structure

---

## 🛠️ Tech Stack

### Language

* **Python 3**

### Programming Concepts

* Object-Oriented Programming (OOP)
* Classes and Objects
* Methods and Functions
* Encapsulation
* Conditional Logic
* Loops
* Input Validation
* Exception Handling

### Interface

* Command-Line Interface (CLI)
* Terminal-based interaction

---

## 🏗️ Application Flow

```text
Start
  │
  ▼
User Authentication
  │
  ▼
PIN Verification
  │
  ├── Invalid PIN → Authentication Failed
  │
  ▼
ATM Main Menu
  │
  ├── Check Balance
  │
  ├── Withdraw Cash
  │
  ├── Deposit Cash
  │
  └── Exit
  │
  ▼
Transaction Processing
  │
  ▼
Updated Account State
```

---

## 💳 Core Operations

### 🔐 Authentication

Users authenticate through a PIN-based login process before accessing ATM operations.

### 💰 Balance Inquiry

Displays the current available account balance.

### 💸 Cash Withdrawal

Allows users to withdraw money while validating the requested amount against available balance and transaction rules.

### 💵 Cash Deposit

Allows users to deposit funds and update the account balance accordingly.

### 📋 Transaction Handling

The application manages transactions through structured methods and validates user input before processing operations.

---

## 🧩 Object-Oriented Structure

The application is organized around object-oriented programming principles.

Core concepts include:

* **Classes** for representing application entities
* **Objects** for maintaining account/application state
* **Methods** for handling ATM operations
* **Encapsulation** for organizing related data and behavior
* **Conditional logic** for transaction validation
* **Exception handling** for handling invalid input and runtime conditions

---

## 📂 Project Structure

```text
ATM_System/
│
├── main.py
└── README.md
```

> Update the file structure above if your repository contains multiple Python files.

---

## 🚀 Getting Started

### Prerequisites

Make sure Python 3 is installed on your system.

Check your Python installation:

```bash
python --version
```

or:

```bash
python3 --version
```

### 1. Clone the repository

```bash
git clone https://github.com/shaheed-khan/ATM_System.git
```

### 2. Navigate to the project directory

```bash
cd ATM_System
```

### 3. Run the application

```bash
python main.py
```

If your main Python file has a different name, replace `main.py` with the correct filename.

---

## 🖥️ Interface

The application runs entirely through the **terminal/command line**.

Users interact with the system through menu-driven options to authenticate and perform ATM operations.

---

## 🔒 Validation & Error Handling

The application handles common transaction and input conditions such as:

* Invalid PIN input
* Invalid menu selections
* Invalid transaction amounts
* Insufficient balance
* Invalid deposit amounts
* Incorrect user input

---

## 📌 Project Status

**Status:** Completed

---

## 👨‍💻 Author

### Shaheed Khan

**Software Developer | Full-Stack Developer | Python & FastAPI | React.js | AI/ML**

* 💼 LinkedIn: [Connect with me on LinkedIn](linkedin.com/in/shaheed-khan-dev/)
* 🐙 GitHub: [@shaheed-khan](https://github.com/shaheed-khan)

---

### ⭐ Explore the Repository

Feel free to explore the source code and the implementation of the ATM system.
