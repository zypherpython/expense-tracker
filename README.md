# 💰 Expense Tracker - Personal Finance Made Simple

> A clean, intuitive desktop expense tracker built with Python. Track your spending, manage categories, and export reports effortlessly.

---

## 📋 Overview

**Expense Tracker** is a lightweight desktop application that helps you take control of your finances. Add expenses with categories, search through your spending history, and export data for analysis—all with a simple, user-friendly interface.

Whether you're tracking daily expenses or analyzing monthly spending patterns, this tool makes personal finance management easy and accessible.

---

## ✨ Key Features

- 💵 **Quick Entry** - Add expenses with description, amount, category, and date
- 🏷️ **Smart Categories** - Organize by Food, Transport, Entertainment, Shopping, Bills, and more
- 🔍 **Instant Search** - Filter expenses by name or category in real-time
- 📊 **Live Totals** - See your total spending and expense count at a glance
- 💾 **Auto-Save** - All data persists locally in JSON format
- 📥 **Export to CSV** - Generate reports for spreadsheet analysis
- 🎯 **Clean UI** - Simple, intuitive interface with no clutter

---

## 🚀 Getting Started

### Requirements
- Python 3.7+
- Tkinter (usually bundled with Python)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/zypherpython/expense-tracker.git
   cd expense-tracker
   ```

2. **Install dependencies** (if any)
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**
   ```bash
   python Expense-Tracker.py
   ```

---

## 💡 How to Use

### Adding an Expense
1. Enter a description (e.g., "Lunch", "Taxi")
2. Enter the amount
3. Pick a category
4. Confirm the date (or use today's date)
5. Click **➕ Add Expense**

### Managing Your Data
- **Search** - Type in the search box to find expenses
- **Delete** - Select an expense and click **🗑️ Delete**
- **Export** - Click **💾 Export** to save as CSV
- **Refresh** - Reset the view anytime

### Where's My Data?
All expenses are saved in `expenses.json` in the app folder. This file is created automatically.

---

## 📁 Project Structure

```
expense-tracker/
├── Expense-Tracker.py     # Main application
├── requirements.txt       # Dependencies
├── README.md              # This file
└── expenses.json          # Your expense data (auto-created)
```

---

## 🛠️ Tech Stack

- **Python 3.7+** - Core language
- **Tkinter** - Desktop GUI
- **JSON** - Data storage
- **CSV** - Report export

---

## 🚧 Roadmap

- [x] Add/delete expenses
- [x] Category filtering
- [x] Real-time search
- [x] CSV export
- [ ] Budget alerts
- [ ] Monthly reports & charts
- [ ] Expense editing
- [ ] SQLite database support
- [ ] Dark mode theme

---

## 📝 About the Developer

🎓 **17-year-old Developer**

Building portfolio projects to learn real-world development. This expense tracker teaches file I/O, data structures, and GUI design—essential skills for any software engineer.

---

## 🤝 Contributing

Found a bug? Have an idea? Contributions welcome!
- Fork the repo
- Create a feature branch
- Submit a pull request

---

## 📜 License

MIT License - Free to use and modify

---

## 📚 Credits

**Code & Design**: Built by myself  
**Documentation**: Enhanced by Copilot

---

**Track your spending. Take control of your finances. 💪**
