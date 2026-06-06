# 💰 Expense Tracker Pro

[![Python Version](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-zypherpython-black)](https://github.com/zypherpython)

A feature-rich desktop expense tracking application built with Python and Tkinter. Easily track, manage, and visualize your daily expenses with a clean, intuitive GUI.

## ✨ Features

- **➕ Add Expenses** - Track expenses with description, amount, category, and date
- **🗂️ Category Support** - Organize expenses by Food, Transport, Entertainment, Shopping, Bills, and more
- **🔍 Search & Filter** - Quickly find expenses by name or category
- **📊 Real-time Total** - Automatic calculation of total expenses
- **💾 Persistent Storage** - Save all data locally using JSON format
- **📥 Export to CSV** - Generate CSV reports for external analysis
- **🎨 Clean UI** - Modern, user-friendly interface with dark theme support
- **✔️ Input Validation** - Ensures data integrity with proper error checking

## 📸 Screenshots

```
┌─────────────────────────────────────────────────┐
│           💰 Expense Tracker Pro               │
├─────────────────────────────────────────────────┤
│ Add New Expense                                 │
│ Description: [___________________]             │
│ Amount (₹): [___________________]              │
│ Category: [Dropdown ▼]                         │
│ Date: [2026-06-06]                             │
│ [➕ Add Expense] [🔄 Clear]                    │
├─────────────────────────────────────────────────┤
│ Search: [_____________]                        │
├─────────────────────────────────────────────────┤
│ 2026-06-06 | Food            | Lunch   | ₹250  │
│ 2026-06-05 | Transport       | Uber    | ₹150  │
│ 2026-06-05 | Entertainment   | Movie   | ₹400  │
│ 2026-06-04 | Bills           | Rent    | ₹5000 │
├─────────────────────────────────────────────────┤
│ [🗑️ Delete] [💾 Export] [🔄 Refresh]          │
├─────────────────────────────────────────────────┤
│ Total: ₹5800.00                               │
│ Expenses: 4                                    │
└─────────────────────────────────────────────────┘
```

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/zypherpython/expense-tracker.git
   cd expense-tracker
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
   Or if you only have Tkinter (usually bundled with Python):
   ```bash
   # For Ubuntu/Debian
   sudo apt-get install python3-tk
   
   # For macOS
   brew install python-tk
   
   # For Windows - Install Python with Tkinter checkbox enabled
   ```

3. **Run the application**
   ```bash
   python expense_tracker.py
   ```

## 📖 Usage

### Adding an Expense
1. Enter a description (e.g., "Lunch", "Taxi fare")
2. Enter the amount in rupees
3. Select a category from the dropdown
4. (Optional) Modify the date if needed
5. Click **➕ Add Expense**

### Managing Expenses
- **Search**: Type in the search box to filter by description or category
- **Delete**: Select an expense and click **🗑️ Delete Selected**
- **Export**: Click **💾 Export to CSV** to save expenses for reporting
- **Refresh**: Click **🔄 Refresh** to reset the view

### Data Storage
All expenses are automatically saved to `expenses.json` in the application directory.

## 📁 File Structure

```
expense-tracker/
├── expense_tracker.py      # Main application
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── LICENSE                # MIT License
└── expenses.json          # Data file (auto-created)
```

## 💾 Data Format

Expenses are stored in JSON format:
```json
[
  {
    "id": "2026-06-06T17:08:56.009",
    "name": "Lunch",
    "amount": 250.0,
    "category": "Food",
    "date": "2026-06-06"
  },
  {
    "id": "2026-06-05T15:30:00",
    "name": "Uber",
    "amount": 150.0,
    "category": "Transport",
    "date": "2026-06-05"
  }
]
```

## 🛠️ Technologies Used

- **Python 3.7+** - Programming language
- **Tkinter** - GUI framework (built-in with Python)
- **JSON** - Data storage
- **CSV** - Export format

## 🎯 Future Enhancements

- [ ] Monthly/yearly expense reports with charts
- [ ] Budget limit alerts
- [ ] Database support (SQLite)
- [ ] Multi-user support
- [ ] Dark mode theme
- [ ] Expense editing functionality
- [ ] Charts and visualizations (Matplotlib integration)
- [ ] Mobile app version
- [ ] Cloud backup and sync

## 🐛 Known Issues

None reported yet! Please report any bugs as GitHub issues.

## 💡 Tips & Tricks

1. **Keyboard Shortcut**: Press `Ctrl+C` to clear input fields quickly
2. **CSV Export**: Use the exported CSV files with Excel or Google Sheets for analysis
3. **Backup**: Regularly backup your `expenses.json` file
4. **Bulk Import**: (Coming soon) Ability to import expenses from CSV

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Zypher Python**
- GitHub: [@zypherpython](https://github.com/zypherpython)
- Created: June 2026

## 🙏 Acknowledgments

- Built with ❤️ using Python and Tkinter
- Inspired by the need for simple expense tracking
- Thanks to the Python community!

## 📞 Support

For support, email support@expensetracker.com or open an issue on GitHub.

---

**⭐ If you find this project helpful, please give it a star!**
