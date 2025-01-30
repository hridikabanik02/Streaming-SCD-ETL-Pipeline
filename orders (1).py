import sqlite3
from datetime import datetime

# Connect to SQLite
conn = sqlite3.connect('assignment2.db')
cursor = conn.cursor()

def process_order(csv_line):
    order_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    order_id, customer_id, amount = csv_line.split(',')

    # TODO: Insert the order into fact_orders
    cursor.execute("""
                   INSERT INTO fact_orders 
                   (order_id, customer_id, order_date, amount)
                   VALUES(?,?,?,?)""", (order_id, customer_id, order_date, amount))

    conn.commit()

if __name__ == "__main__":
    while True:
        # Simulate order input from command line in CSV format
        csv_input = input("Enter order data (CSV format: order_id,customer_id,amount): ")
        
        # Process order record
        process_order(csv_input)