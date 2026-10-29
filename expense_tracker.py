import csv
import os
from collections import defaultdict
from datetime import datetime

CSV_FILE = "expenses.csv"
FIELDS = ["Date", "Category", "Amount", "Description"]

def init_file():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            writer.writeheader()

def add_expense():
    print("\n--- Add Expense ---")
    date = input("Date (YYYY-MM-DD) or press Enter for today: ").strip()
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")
    category = input("Category (Food, Travel, Shopping, Bills): ").strip().title()
    if not category:
        category = "Other"
    try:
        amount = float(input("Amount: Rs. "))
    except:
        print("Invalid amount!")
        return
    desc = input("Description: ").strip()

    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writerow({"Date": date, "Category": category, "Amount": amount, "Description": desc})
    print(f"Saved! {category} - Rs.{amount}")

def view_expenses():
    print("\n--- All Expenses ---")
    with open(CSV_FILE, "r") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        if not rows:
            print("No expenses yet!")
            return
        for i, row in enumerate(rows, 1):
            print(f"{i}. {row['Date']} | {row['Category']:10} | Rs.{row['Amount']:7} | {row['Description']}")

def filter_expenses():
    print("\n--- Filter by Category ---")
    cat = input("Enter category: ").strip().title()
    found = False
    with open(CSV_FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Category"].lower() == cat.lower():
                print(f"{row['Date']} | {row['Category']} | Rs.{row['Amount']} | {row['Description']}")
                found = True
    if not found:
        print(f"No expenses for {cat}")

def category_summary():
    print("\n--- Category Summary ---")
    summary = defaultdict(float)
    total = 0
    with open(CSV_FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                amt = float(row["Amount"])
                summary[row["Category"]] += amt
                total += amt
            except:
                pass
    if not summary:
        print("No data!")
        return
    for cat, amt in summary.items():
        print(f"{cat:12} : Rs. {amt:.2f}")
    print(f"\nTotal Spent: Rs. {total:.2f}")

init_file()
while True:
    print("\n===== Personal Expense Tracker =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Filter by Category")
    print("4. Category Summary")
    print("5. Exit")
    ch = input("Choose 1-5: ")

    if ch == "1":
        add_expense()
    elif ch == "2":
        view_expenses()
    elif ch == "3":
        filter_expenses()
    elif ch == "4":
        category_summary()
    elif ch == "5":
        print("Bye! Data saved in expenses.csv")
        break
    else:
        print("Invalid choice!")