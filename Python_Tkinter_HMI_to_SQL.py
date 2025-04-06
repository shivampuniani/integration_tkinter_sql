from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pyodbc
import datetime
import configparser


#change width and height value here for hmi size
w = 600
h = 600

# Read configuration from config.ini
def get_db_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    
    db_config = {
        'server': config.get('database', 'server'),
        'database': config.get('database', 'database'),
        'username': config.get('database', 'username'),
        'password': config.get('database', 'password'),
        'field1' : config.get('fields', 'field1'),
        'field2' : config.get('fields', 'field2'),
        'field3' : config.get('fields', 'field3'),
        'field4' : config.get('fields', 'field4'),
        'field5' : config.get('fields', 'field5'),
        'field6' : config.get('fields', 'field6'),
        'field7' : config.get('fields', 'field7'),
        'field8' : config.get('fields', 'field8'),
        'w' : config.get('dimensions', 'w'),
        'h' : config.get('dimensions', 'h')
    }
    return db_config
test_no_track = ''
def db_connection(server, database, uid, pwd):
    
    conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
        f'SERVER={server};'
        f'DATABASE={database};'
        f'UID={uid};'
        f'PWD={pwd}'
    )

    return conn

class MyApp:
    def __init__(self, root):
        try:
            db_config = get_db_config()
            field1 = db_config["field1"]
            field2 = db_config["field2"]
            field3 = db_config["field3"]
            field4 = db_config["field4"]
            field5 = db_config["field5"]
            field6 = db_config["field6"]
            field7 = db_config["field7"]
            field8 = db_config["field8"]

            w = db_config["w"]
            h = db_config["h"]

            
            self.root = root
            hmi_bg = StringVar(value='#FABC36')
            root['bg'] = (hmi_bg.get())
            self.root.geometry("%dx%d" % (int(w), int(h)))
            self.root.title("Sieger Data Entry")
            self.root.resizable(False, False)
            # root.iconbitmap("TG_badge.jfif")
            
            self.header = ttk.Label(root, font=('Century 32'), text="HMI :", background = hmi_bg.get())
            self.header.pack()
            self.header.place(x=200, y=10)
            self.header2 = ttk.Label(root, font=('Century 40'), text="1", background = hmi_bg.get())
            self.header2.pack()
            self.header2.place(x=360, y=0)

            self.field1_label = ttk.Label(root, font=('Century 11'), text=field1 +": ")
            self.field1_label.pack()
            self.field1_label.place(x=30, y=80)
            self.field1_entry = ttk.Entry(root, font=('Century 11'), width=18)
            self.field1_entry.pack()
            self.field1_entry.place(x=100, y=80)
     

            self.field2_label = ttk.Label(root, font=('Century 11'), text=field2 +": ", background = hmi_bg.get())
            self.field2_label.pack()
            self.field2_label.place(x=30, y=130)
            self.field2_entry = ttk.Entry(root, font=('Century 11'), width=18)
            self.field2_entry.pack()
            self.field2_entry.place(x=100, y=130)
     
            self.field3_label = ttk.Label(root, font=('Century 11'), text=field3 +": ", background = hmi_bg.get())
            self.field3_label.pack()
            self.field3_label.place(x=30, y=180)
            self.field3_entry = ttk.Entry(root, font=('Century 11'), width=13)
            self.field3_entry.pack()
            self.field3_entry.place(x=140, y=180)
     
            self.field4_label = ttk.Label(root, font=('Century 11'), text=field4 +": ", background = hmi_bg.get())
            self.field4_label.pack()
            self.field4_label.place(x=30, y=230)
            options = ["option1", "option2", "option3", "option4"]
            self.field4_entry = ttk.Combobox(root, state='readonly', values=options, width=14)
            self.field4_entry.pack()
            self.field4_entry.place(x=140, y=230)
     
            ##### right
            self.field5_label = ttk.Label(root, font=('Century 11'), text=field5 +": ")
            self.field5_label.pack()
            self.field5_label.place(x=330, y=80)
            self.field5_entry = ttk.Entry(root, font=('Century 11'), width=18)
            self.field5_entry.pack()
            self.field5_entry.place(x=410, y=80)
     
            self.field6_label = ttk.Label(root, font=('Century 11'), text=field6 +": ", background = hmi_bg.get())
            self.field6_label.pack()
            self.field6_label.place(x=330, y=130)
            self.field6_entry = ttk.Entry(root, font=('Century 11'), width=13)
            self.field6_entry.pack()
            self.field6_entry.place(x=442, y=130)
     
            self.field7_label = ttk.Label(root, font=('Century 11'), text=field7 +": ", background = hmi_bg.get())
            self.field7_label.pack()
            self.field7_label.place(x=330, y=180)
            self.field7_entry = ttk.Entry(root, font=('Century 11'), width=12)
            self.field7_entry.pack()
            self.field7_entry.place(x=457, y=180)
     
            self.field8_label = ttk.Label(root, font=('Century 11'), text=field8 +": ", background = hmi_bg.get())
            self.field8_label.pack()
            self.field8_label.place(x=330, y=230)
            self.field8_entry = ttk.Entry(root, font=('Century 11'), width=5)
            self.field8_entry.pack()
            self.field8_entry.place(x=512, y=230)

            self.tree = ttk.Treeview(root, column=("c1", "c2", "c3", "c4","c5", "c6", "c7", "c8"), show='headings', height = 12)
            self.tree.column("#1", anchor=CENTER, stretch = NO, width = 80)
            self.tree.heading("#1", text=field1)
            self.tree.column("#2", anchor=CENTER, stretch = NO, width = 80)
            self.tree.heading("#2", text=field2)
            self.tree.column("#3", anchor=CENTER, stretch = NO, width = 72)
            self.tree.heading("#3", text=field3)
            self.tree.column("#4", anchor=CENTER, stretch = NO, width = 80)
            self.tree.heading("#4", text=field4)
            self.tree.column("#5", anchor=CENTER, stretch = NO, width = 60)
            self.tree.heading("#5", text=field5)
            self.tree.column("#6", anchor=CENTER, stretch = NO, width = 60)
            self.tree.heading("#6", text=field6)
            self.tree.column("#7", anchor=CENTER, stretch = NO, width = 95)
            self.tree.heading("#7", text=field7)
            self.tree.column("#8", anchor=CENTER, stretch = NO, width = 60)
            self.tree.heading("#8", text=field8)
            self.tree.pack()
            self.tree.place(x=5, y=320)
     
            self.field2_entry.bind('<Down>', self.focus_next_entry)
            self.field2_entry.bind('<Up>', self.focus_prev_entry)
            self.field3_entry.bind('<Down>', self.focus_next_entry)
            self.field3_entry.bind('<Up>', self.focus_prev_entry)
            self.field4_entry.bind('<Down>', self.focus_next_entry)
            self.field4_entry.bind('<Up>', self.focus_prev_entry)
            self.field5_entry.bind('<Down>', self.focus_next_entry)
            self.field5_entry.bind('<Up>', self.focus_prev_entry)
            self.field8_entry.bind('<Down>', self.focus_next_entry)
            self.field8_entry.bind('<Up>', self.focus_prev_entry)
            self.field7_entry.bind('<Down>', self.focus_next_entry)
            self.field7_entry.bind('<Up>', self.focus_prev_entry)
     
            style = ttk.Style()
            style.configure('Custom.TButton',
                            foreground='black',
                            background='green',
                            padding=(8, 4),
                            borderwidth=2,
                            relief='groove',
                            font=('Century', 12))
            self.send_btn = ttk.Button(root, text="Submit", style='Custom.TButton', command= lambda: self.submit_data(db_config))
            self.send_btn.pack()
            self.send_btn.place(x=250, y=280)
            self.get_btn = ttk.Button(root, text="Refresh", command= lambda: self.refresh_data(db_config))
            self.get_btn.pack()
            self.get_btn.place(x=500, y=290)
        except Exception as e:
            log_report(e)
            
 
    def focus_next_entry(self, event):
        event.widget.tk_focusNext().focus()
        return "break"
 
    def focus_prev_entry(self, event):
        event.widget.tk_focusPrev().focus()
        return "break"
    
    def error_box(self, err_msg):
        log_file = r".\log_file.txt"
        with open(log_file, 'a') as log:
            log.write(f"{datetime.datetime.now()} + ' | ' +  {err_msg} \n")
        messagebox.showerror('Error !!!', err_msg)

    def log_report(e):
        # log_file = 'log.txt'
        log_file = r".\log_file.txt"
        with open(log_file, 'a') as log:
            log.write(f"{datetime.datetime.now()} + ' | ' +  {e} \n")
       
    def datetime_shift(self):
        t_now = str(datetime.datetime.now())
        t_now = t_now[:19]
        shift = ''
        current_time = datetime.datetime.now().time()
 
        shift_c_start = datetime.time(23, 0)
        shift_c_end = datetime.time(6, 59)
        shift_a_start = datetime.time(7, 0)
        shift_a_end = datetime.time(14, 59)
        shift_b_start = datetime.time(15, 0)
        shift_b_end = datetime.time(22, 59)
 
        if shift_c_start <= current_time <= shift_c_end:
            shift = 'C'
        elif shift_a_start <= current_time <= shift_a_end:
            shift = 'A'
        elif shift_b_start <= current_time <= shift_b_end:
            shift = 'B'
        else:
            shift = ''
        return t_now, shift

    def refresh_data(self, db_config):
            try:
                cnxn = db_connection(db_config["server"], db_config["database"], db_config["username"], db_config["password"])
                cur = cnxn.cursor()
                outputListData = []
                rows = cur.execute("""SELECT TOP (10) [field1_value] ,[field2_value] ,[field3_value] ,[field4_value] ,[field5_value] ,[field6_value] ,[field7_value] ,[field8_value] FROM [dbo].[Test_TKINTER] order by timestamp desc""")
                outputListData = [', '.join(map(str, row)).rstrip(',') for row in rows]  
                for row in outputListData:
                    self.tree.insert("", END, values=row)
                cnxn.close()
            except Exception as e:
                self.error_box("Error while refreshing data to DB. " + str(e))
 
    def submit_data(self, db_config):
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        field1_value = self.field1_entry.get()
        field2_value = self.field2_entry.get()
        field3_value = self.field3_entry.get()
        field4_value = self.field4_entry.get()
        field5_value = self.field5_entry.get()
        field6_value = self.field6_entry.get()
        field7_value = self.field7_entry.get()
        field8_value = self.field8_entry.get()
        timestamp, shift = self.datetime_shift()
       
        if(field2_value != "" and field5_value != ""  and field3_value != "" and field4_value != "" and field7_value != ""  and shift != "" and timestamp != ""  and field8_value != ""): # and field5_value != ""):
 
            try:
                cnxn = db_connection(db_config["server"], db_config["database"], db_config["username"], db_config["password"])
                cur = cnxn.cursor()
                
                query = f"INSERT INTO [dbo].[Test_TKINTER] ([field1_value], [field5_value],[field2_value], [field3_value], [field4_value], [field7_value], [shift], [timestamp], [field8_value], [field6_value], [flag]) VALUES ('{field1_value}','{field5_value}', '{field2_value}',  '{field3_value}', '{field4_value}', '{field7_value}', '{shift}', '{timestamp}',  '{field8_value}', '{field6_value}', '0')"
                #query = "INSERT INTO [sieger_DB] ([field1_value], [field5_value], [field2_value], [confirmed_qty], [gross_weight], [net_weight], [field3_value], [field4_value], [field7_value], [carton_mat_code], [salary_code], [gi_mat_1], [gi_mat_2], [gi_mat_3], [gi_mat_4], [gi_mat_5], [plant_id], [shift], [timestamp], [flag]) VALUES ('4111031197', '100', 'VB19FK0001', '1000', '9999', '9999', '999', 'APAC 1', '999', '99', '41014050', '314000610', '314000611', '314000612', '314000613', '314000614', 'tyb8', 'B', '2024-03-01', '0')"
                cur.execute(query)
                cur.commit()
 
                self.field1_entry.delete(0, END)
                self.field6_entry.delete(0, END)
                self.field2_entry.delete(0, END)
                self.field3_entry.delete(0, END)
                self.field4_entry.delete(0, END)
                self.field8_entry.delete(0, END)
                self.field7_entry.delete(0, END)
                self.field5_entry.delete(0, END)
                
                cur.close()
                cnxn.close()
            except Exception as e:
                self.error_box("Error while pushing data to DB. " + str(e))
        else:
            err_msg = "All Fields are Mandatory"
            self.error_box(err_msg=err_msg)
 
root = Tk()
app = MyApp(root)
root.mainloop()
