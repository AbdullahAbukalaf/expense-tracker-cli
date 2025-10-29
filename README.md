# 🧾 Expense Tracker CLI (Interactive TUI)

A simple, interactive Expense Tracker built in Python, running directly in your terminal — no browser, no setup, no nonsense.

It helps you track daily expenses, view totals, filter by category, edit entries, and see monthly summaries in a clean, keyboard-driven interface.

---

## 🚀 Features

* ✅ Add new expenses (title, amount, description, category)
* ✅ Edit existing expenses *(new in v0.2.0)*
* ✅ List all expenses in a neat table view
* ✅ View monthly summary *(new in v0.2.0)*
* ✅ Filter expenses by category
* ✅ Delete entries
* ✅ See monthly total at the top
* ✅ Auto-save to a local `data.json` file
* ✅ Clean modular structure (`models` / `storage` / `commands` / `ui` / `utils`)
* ✅ Colorful, aligned CLI interface with keyboard controls

---

## 🌟 Preview

```text
=====================================================================
Expense Tracker CLI v0.2.0                   October 2025
Total this month: 28.65 JOD
=====================================================================

ID    TITLE            DESCRIPTION                          AMOUNT      CATEGORY         DATE        
---------------------------------------------------------------------------------------------------- 
#1    Coffee           morning Coffee                       2.75 JOD    food             2025-10-29  
#2    Uber             Uber to work                         3.00 JOD    transport        2025-10-29  
#3    Groceries        Groceries for apartment              22.90 JOD   food             2025-10-29  

[a] Add   [e] Edit   [d] Delete   [f] Filter   [m] Monthly   [q] Quit
>
```

### 🧾 Monthly Summary Example

```text
================ Monthly Summary ================
Month: October 2025

Total spent:  28.65 JOD
Transactions: 3

Spending by category:
--------------------------------
food        : 25.65 JOD
transport   :  3.00 JOD

Press Enter to continue...
```

No typing long commands — just press keys to interact.

---

## 🗂 Project Structure

```text
expense-tracker-cli/
├─ main.py            # Entry point (starts the app)
├─ commands.py        # Logic for add/edit/delete/filter/summary
├─ models.py          # Expense model + create_expense()
├─ storage.py         # Load/save/update data in data.json
├─ ui.py              # Draws interactive terminal interface (TUI)
├─ utils.py           # Helpers (formatting, colors, etc.)
├─ data.json          # Local database (auto-created)
├─ version.py         # Version info (v0.2.0)
└─ README.md          # Project documentation
```

---

## ⚙️ Installation

Clone the repo:

```bash
git clone https://github.com/AbdullahAbukalaf/expense-tracker-cli.git
cd expense-tracker-cli
```

(Recommended) create a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate      # on Windows
source venv/bin/activate   # on macOS/Linux
```

Install dependencies (if you use any):

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the App

Start the program:

```bash
python main.py
```

You’ll immediately see the dashboard:

```text
=====================================================================
Expense Tracker CLI v0.2.0                   October 2025
Total this month: ...
=====================================================================
```

Then control it using:

* **[a]** → Add new expense
* **[e]** → Edit existing expense *(v0.2.0)*
* **[d]** → Delete selected expense
* **[f]** → Filter by category
* **[m]** → View monthly summary *(v0.2.0)*
* **[q]** → Quit the program

---

## 💾 Data Storage

All expenses are saved in a `data.json` file at the project root.
You can back it up, reset it, or even sync it later to cloud storage.

Example `data.json`:

```json
[
  {
    "id": 3,
    "title": "Groceries",
    "description": "Groceries for apartment",
    "amount": 22.90,
    "category": "food",
    "date": "2025-10-29"
  }
]
```

---

## 🧱 Architecture Overview

| Layer       | File          | Responsibility                                          |
| ----------- | ------------- | ------------------------------------------------------- |
| Interface   | `ui.py`       | Displays interactive screen & listens for user input    |
| Commands    | `commands.py` | Implements add / edit / delete / filter / summary logic |
| Data Model  | `models.py`   | Defines `Expense` structure & creation helper           |
| Storage     | `storage.py`  | Handles reading, writing, and updating `data.json`      |
| Utilities   | `utils.py`    | Formats text, colors, and table rows                    |
| Entry Point | `main.py`     | Starts the app and manages main loop                    |

---

## 🔮 Future Plans

* [ ] Export to CSV
* [ ] Budget alerts per category
* [ ] Monthly comparisons (previous vs current month)
* [ ] Currency selector (JOD / USD / EUR)
* [ ] Cloud sync with AWS S3

---

## 🧭 Version History

**v0.2.0 (current)**

* Added `[e]` Edit command
* Added `[m]` Monthly summary view
* Improved CLI UI (colors, alignment, version header)
* Cleaned architecture and logic separation

**v0.1.0 (previous)**

* Initial release (Add, Delete, Filter, and Total features)

---

## 📜 License

MIT License © 2025 **Abdullah Abukalaf**

GitHub: [@AbdullahAbukalaf](https://github.com/AbdullahAbukalaf)

---

