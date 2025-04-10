# Sieger Data Entry HMI with SQL Server Integration

This program is a graphical user interface (GUI) application built with Python's Tkinter library. It allows users to input data through various fields in a GUI, and submit the data to a SQL Server database. The application retrieves and displays the last 10 records from the database in a table for easy viewing.

## Features

- **Graphical User Interface (GUI)**: Designed with Tkinter to provide a user-friendly interface for data entry.
- **Dynamic Data Display**: Displays the latest 10 records from the SQL Server database in a table.
- **Database Integration**: Uses `pyodbc` to connect and interact with SQL Server.
- **Data Validation**: Ensures all fields are filled before submitting data to the database.
- **Error Logging**: Logs errors with timestamps for troubleshooting.
- **Customised Field name**: Mention the required field name in the config.ini same will be displayed in HMI.


## Setup


1. Clone the repository:
   ```bash
   git clone https://github.com/shivampuniani/integration_tkinter_sql.git  

2. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt

3. Configure the database connection:

Update the connection details in the config.ini file with your SQL Server credentials. Here's the format:    

   
   [database]  
   server = NOT-CONNECTED\TEW_SQLEXPRESS  
   database = Test_Database  
   username = sa  
   password = 12345678  
     
   [fields]  
   field1 = field1  
   field2 = field2  
   field3 = field3  
   field4 = field4  
   field5 = field5  
   field6 = field6  
   field7 = field7  
   field8 = field8  
     
   [dimensions]  
   w = 600  
   h = 600 

4. Run the script:
   ```bash
   Python_Tkinter_HMI_to_SQL.py


Tkinter_HMI-SQL-Integration-project/  
│  
├── Python_Tkinter_HMI_to_SQL.py                                 # Your main Python program  
├── requirements.txt                                             # Python dependencies  
├── README.md                                                    # Project documentation  
├── config.ini                                                   # config file to store and configure sql server and file data   
├── .gitignore                                                   # Git ignore rules  
└── log_file.txt                                                 # Log file (will be generated when running the program)  
