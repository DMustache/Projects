import pandas as pd
import pyodbc

data = pd.read_csv(r'C:\Users\Dmitry\Documents\test.csv', sep=';', encoding='cp1251')
df = pd.DataFrame(data, columns=['id','room_number','room_description','event_type_name', 'event_type_start','event_type_end','event_type_description','event_media','group_name'])

conn = pyodbc.connect('Driver={SQL Server};'
'Server=DMUSTACHE\SQLEXPRESS;'
'Database=InClassServer;'
'Trusted_Connection=yes;')
cursor = conn.cursor()

#cursor.execute('create table timetable_data (id int primary KEY NOT NULL, room_number int NOT NULL, room_description varchar(30) NULL, event_type_name varchar(25) NOT NULL, event_type_start time NOT NULL, event_type_end time NOT NULL, event_type_description varchar(30) NULL, event_media text NULL, group_name varchar(5) NOT NULL)')

for row in df.itertuples():
    cursor.execute('''
    insert into InClassServer.datetime_data (id, room_number, room_description, event_type_start, event_type_end, event_type_description, event_media, group_name)
    VALUES (?,?,?,?,?,?,?,?,?)''',
    row.id,
    row.room_number,
    row.room_description,
    row.event_type_name,
    row.event_type_start,
    row.event_type_end,
    row.event_type_description,
    row.event_media,
    row.group_name
)
conn.commit()