# Bookshop-Management-System

A Python + MySQL project to manage a bookshop with separate Admin and Customer modules.

## Features
- Admin: manage customer accounts, update book genres, change credentials.
- Customer: create account, login with validation, browse and order books, generate bill.
- Database integration with MySQL using `mysql-connector`.

## Tech Stack
- Python
- MySQL
- CSV for admin credentials
- Random module for customer ID generation

## How to Run
1. Clone the repo.
2. Ensure MySQL server is running.
3. Update DB credentials in `start.py`.
4. Run the program:
   ```bash
   python start.py
