import sqlite3
from datetime import datetime

# Connect to SQLite
conn = sqlite3.connect('assignment2.db')
cursor = conn.cursor()

def transform_customer_data(data):
        # Basic transformation: Strip any leading/trailing whitespace
        # TODO: Your transformation code in Python
        data[0] = data[0].strip() #Assuming customer_id
        data[1] = data[1].strip() #Assuming name
        data[2] = data[2].strip() #Assuming city
        #print(data[0]+data[1]+data[2])
       
        return data

def process_customer(csv_line):
    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    customer_id, name, city = transform_customer_data(csv_line.split(','))
    
    # TODO: Query the current customer data to check if this is a new customer or an update
    cursor.execute("""SELECT * FROM dim_customers 
                      WHERE customer_id = ? AND is_current = 1 """, (customer_id))

    current_record = cursor.fetchone()

    if current_record:
        if current_record[1] != name or current_record[2] != city:
            # TODO: Expire the old record
            cursor.execute(""" UPDATE dim_customers 
                        SET end_date  = ? , is_current = 0
                        WHERE customer_id = ? AND is_current = 1""", (current_date,customer_id))

            # TODO: Insert the new record
            cursor.execute(""" INSERT INTO dim_customers 
                        VALUES(?,?,?,?,NULL,1)""", (customer_id,name,city,current_date))
    else:
        # New customer, insert into dim_customers
        cursor.execute(""" INSERT INTO dim_customers 
                       VALUES(?,?,?,?,NULL,1)""", (customer_id,name,city,current_date))
    conn.commit()

if __name__ == "__main__":
    while True:
        # Simulate customer input from the command line in CSV format
        csv_input = input("Enter customer data (CSV format:customer_id,name,city): ")
        # Process customer record
        process_customer(csv_input)
