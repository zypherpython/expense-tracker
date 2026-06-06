import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
import csv
from datetime import datetime
from pathlib import Path


class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("💰 Expense Tracker Pro")
        self.root.geometry("600x650")
        self.root.resizable(False, False)
        
        # Data file for persistence
        self.data_file = Path("expenses.json")
        self.expenses = self.load_expenses()
        
        # Configure style
        style = ttk.Style()
        style.theme_use('clam')
        
        self.setup_ui()
        self.refresh_display()
    
    def setup_ui(self):
        """Setup the user interface."""
        # Title
        title = tk.Label(self.root, text="💰 Expense Tracker Pro", 
                        font=("Arial", 18, "bold"), fg="#2c3e50")
        title.pack(pady=10)
        
        # Input Frame
        input_frame = ttk.LabelFrame(self.root, text="Add New Expense", padding=10)
        input_frame.pack(fill="x", padx=10, pady=10)
        
        # Name
        ttk.Label(input_frame, text="Description:").grid(row=0, column=0, sticky="w", pady=5)
        self.entry_name = ttk.Entry(input_frame, width=30)
        self.entry_name.grid(row=0, column=1, pady=5, padx=5)
        
        # Amount
        ttk.Label(input_frame, text="Amount (₹):").grid(row=1, column=0, sticky="w", pady=5)
        self.entry_amount = ttk.Entry(input_frame, width=30)
        self.entry_amount.grid(row=1, column=1, pady=5, padx=5)
        
        # Category
        ttk.Label(input_frame, text="Category:").grid(row=2, column=0, sticky="w", pady=5)
        self.category_var = tk.StringVar()
        self.category_combo = ttk.Combobox(input_frame, textvariable=self.category_var,
                                           values=["Food", "Transport", "Entertainment", 
                                                   "Shopping", "Bills", "Other"],
                                           width=28, state="readonly")
        self.category_combo.grid(row=2, column=1, pady=5, padx=5)
        self.category_combo.set("Other")
        
        # Date (optional)
        ttk.Label(input_frame, text="Date (YYYY-MM-DD):").grid(row=3, column=0, sticky="w", pady=5)
        self.entry_date = ttk.Entry(input_frame, width=30)
        self.entry_date.insert(0, datetime.now().strftime("%Y-%m-%d"))
        self.entry_date.grid(row=3, column=1, pady=5, padx=5)
        
        # Button Frame
        btn_frame = ttk.Frame(input_frame)
        btn_frame.grid(row=4, column=0, columnspan=2, pady=10, sticky="ew")
        
        ttk.Button(btn_frame, text="➕ Add Expense", command=self.add_expense).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="🔄 Clear", command=self.clear_inputs).pack(side="left", padx=5)
        
        # Search Frame
        search_frame = ttk.Frame(self.root)
        search_frame.pack(fill="x", padx=10, pady=5)
        
        ttk.Label(search_frame, text="Search:").pack(side="left", padx=5)
        self.search_var = tk.StringVar()
        self.search_var.trace("w", lambda *args: self.search_expenses())
        search_entry = ttk.Entry(search_frame, textvariable=self.search_var, width=30)
        search_entry.pack(side="left", padx=5)
        
        # Listbox Frame
        list_frame = ttk.LabelFrame(self.root, text="Expenses List", padding=5)
        list_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(list_frame)
        scrollbar.pack(side="right", fill="y")
        
        self.listbox = tk.Listbox(list_frame, yscrollcommand=scrollbar.set, 
                                  font=("Arial", 10), height=12)
        self.listbox.pack(fill="both", expand=True, side="left")
        scrollbar.config(command=self.listbox.yview)
        
        # Button Frame
        action_frame = ttk.Frame(self.root)
        action_frame.pack(fill="x", padx=10, pady=10)
        
        ttk.Button(action_frame, text="🗑️ Delete Selected", command=self.delete_expense).pack(side="left", padx=5)
        ttk.Button(action_frame, text="💾 Export to CSV", command=self.export_csv).pack(side="left", padx=5)
        ttk.Button(action_frame, text="🔄 Refresh", command=self.refresh_display).pack(side="left", padx=5)
        
        # Total Frame
        total_frame = ttk.Frame(self.root, relief="sunken", padding=10)
        total_frame.pack(fill="x", padx=10, pady=10)
        
        self.label_total = tk.Label(total_frame, text="Total: ₹0.00", 
                                    font=("Arial", 14, "bold"), fg="#27ae60")
        self.label_total.pack()
        
        self.label_count = tk.Label(total_frame, text="Expenses: 0", 
                                   font=("Arial", 10), fg="#7f8c8d")
        self.label_count.pack()
    
    def add_expense(self):
        """Add a new expense."""
        name = self.entry_name.get().strip()
        amount_str = self.entry_amount.get().strip()
        category = self.category_var.get()
        date = self.entry_date.get().strip()
        
        if not name or not amount_str:
            messagebox.showwarning("Input Error", "Please enter description and amount")
            return
        
        try:
            amount = float(amount_str)
            if amount <= 0:
                raise ValueError("Amount must be positive")
        except ValueError:
            messagebox.showwarning("Input Error", "Please enter a valid positive amount")
            return
        
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            messagebox.showwarning("Input Error", "Invalid date format. Use YYYY-MM-DD")
            return
        
        expense = {
            "id": datetime.now().isoformat(),
            "name": name,
            "amount": amount,
            "category": category,
            "date": date
        }
        
        self.expenses.append(expense)
        self.save_expenses()
        self.refresh_display()
        self.clear_inputs()
        messagebox.showinfo("Success", f"Added: {name} - ₹{amount}")
    
    def delete_expense(self):
        """Delete selected expense."""
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showwarning("Selection Error", "Please select an expense to delete")
            return
        
        if messagebox.askyesno("Confirm", "Are you sure you want to delete this expense?"):
            index = selected[0]
            self.expenses.pop(index)
            self.save_expenses()
            self.refresh_display()
            messagebox.showinfo("Success", "Expense deleted")
    
    def clear_inputs(self):
        """Clear input fields."""
        self.entry_name.delete(0, tk.END)
        self.entry_amount.delete(0, tk.END)
        self.entry_date.delete(0, tk.END)
        self.entry_date.insert(0, datetime.now().strftime("%Y-%m-%d"))
        self.category_combo.set("Other")
    
    def refresh_display(self):
        """Refresh the expense list display."""
        self.listbox.delete(0, tk.END)
        total = 0
        
        for expense in self.expenses:
            name = expense["name"]
            amount = expense["amount"]
            category = expense["category"]
            date = expense["date"]
            item = f"{date} | {category:15} | {name:20} | ₹{amount:.2f}"
            self.listbox.insert(tk.END, item)
            total += amount
        
        self.label_total.config(text=f"Total: ₹{total:.2f}")
        self.label_count.config(text=f"Expenses: {len(self.expenses)}")
    
    def search_expenses(self):
        """Search expenses by name or category."""
        search_term = self.search_var.get().lower()
        self.listbox.delete(0, tk.END)
        total = 0
        count = 0
        
        for expense in self.expenses:
            if (search_term in expense["name"].lower() or 
                search_term in expense["category"].lower()):
                name = expense["name"]
                amount = expense["amount"]
                category = expense["category"]
                date = expense["date"]
                item = f"{date} | {category:15} | {name:20} | ₹{amount:.2f}"
                self.listbox.insert(tk.END, item)
                total += amount
                count += 1
        
        if search_term:
            self.label_total.config(text=f"Search Total: ₹{total:.2f}")
            self.label_count.config(text=f"Found: {count}")
        else:
            self.refresh_display()
    
    def export_csv(self):
        """Export expenses to CSV file."""
        if not self.expenses:
            messagebox.showwarning("No Data", "No expenses to export")
            return
        
        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
            initialfile=f"expenses_{datetime.now().strftime('%Y%m%d')}.csv"
        )
        
        if not file_path:
            return
        
        try:
            with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['Date', 'Category', 'Description', 'Amount']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                
                for expense in self.expenses:
                    writer.writerow({
                        'Date': expense['date'],
                        'Category': expense['category'],
                        'Description': expense['name'],
                        'Amount': expense['amount']
                    })
            
            messagebox.showinfo("Success", f"Exported to {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export: {str(e)}")
    
    def save_expenses(self):
        """Save expenses to JSON file."""
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(self.expenses, f, indent=2, ensure_ascii=False)
    
    def load_expenses(self):
        """Load expenses from JSON file."""
        if self.data_file.exists():
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return []
        return []


if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTracker(root)
    root.mainloop()
