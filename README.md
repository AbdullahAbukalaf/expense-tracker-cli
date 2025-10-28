# 🧾 Expense Tracker CLI (Interactive TUI)

A simple, interactive Expense Tracker built in Python, running directly in your terminal — no browser, no setup, no nonsense.

It helps you track daily expenses, view totals, and filter by category in a clean, keyboard-driven interface.

---

## 🚀 Features

* ✅ Add new expenses (title, amount, category)
* ✅ List all expenses in a neat table view
* ✅ See monthly total at the bottom
* ✅ Filter expenses by category
* ✅ Delete entries
* ✅ Auto-save to a local `data.json` file
* ✅ Clean modular structure (`models` / `storage` / `utils` / `ui`)

---

## 🌟 Preview

```text
┌ Expenses (October) ┐
│ ID  Title        Amount   Category     Date
│ 1   Coffee       2.75     food         2025-10-28
│ 2   Uber to work 3.00     transport    2025-10-28
│ 3   Groceries    22.90    food         2025-10-28
└───────────────────────────────────────────────┘

Total this month: 28.65 JOD

[a] Add   [d] Delete   [f] Filter by category   [q] Quit
```

No typing long commands — just press keys to interact.

---

## 🗂 Project Structure

```text
expense-tracker-cli/
├─ main.py            # Entry point (starts the UI)
├─ commands.py        # Logic for add/delete/filter/total
├─ models.py          # Expense model + create_expense()
├─ storage.py         # Load/save data to data.json
├─ ui.py              # Draws interactive terminal interface (TUI)
├─ utils.py           # Helpers (format money, etc.)
├─ data.json          # Local database (auto-created)
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

Install dependencies:

```bash
pip install textual rich
```

---

## ▶️ Run the App

Start the program:

```bash
python main.py
```

You’ll immediately see the dashboard:

```text
┌ Expenses (October) ┐
│ ... data rows ...  │
└────────────────────┘

Total this month: ...
```

Then control it using:

* **[a]** → Add new expense
* **[d]** → Delete selected expense
* **[f]** → Filter by category
* **[q]** → Quit

---

## 💾 Data Storage

All expenses are saved in a `data.json` file at the project root.
You can back it up, reset it, or even sync it later to cloud storage.

Example `data.json`:

```json
[
  {
    "id": 1,
    "title": "Coffee",
    "amount": 2.75,
    "category": "food",
    "date": "2025-10-28T14:32:10"
  }
]
```

---

## 🧱 Architecture Overview

| Layer       | File          | Responsibility                                        |
| ----------- | ------------- | ----------------------------------------------------- |
| Interface   | `ui.py`       | Displays interactive screen & listens for key presses |
| Commands    | `commands.py` | Implements add / delete / filter / total logic        |
| Data Model  | `models.py`   | Defines `Expense` structure & creation helper         |
| Storage     | `storage.py`  | Handles reading & writing `data.json`                 |
| Utilities   | `utils.py`    | Formats text, currency, and table rows                |
| Entry Point | `main.py`     | Starts the UI and initializes app state               |

---

## 🔮 Future Plans

* [ ] Category analytics (charts & totals)
* [ ] Monthly summaries
* [ ] Export to CSV / Excel
* [ ] Currency setting (JOD / USD / EUR)
* [ ] Cloud sync with AWS S3

---

