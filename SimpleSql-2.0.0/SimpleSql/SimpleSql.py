#  -----------------
# |                 |
# |   By @Kia88DC   |
# |                 |
#  -----------------
__version__ = "2.0.0"

class sql():
    def __init__(self, db_name:str) -> None:
        import sqlite3
        self.con = sqlite3.connect(db_name)
        self.cur = self.con.cursor()
        self.data = {}

    def sql_table(self, table_name:str, columns:str) -> None:
        '''
        table_name = the name of the table
        columns = the columns(NAME TYPE,...) e.g: 'id iteger PRIMARY KEY,name text,...'
        '''
        self.data[table_name] = []
        for item in columns.split(','):
            self.data[table_name].append(item.split(' ')[0])
        self.cur.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})")
        self.con.commit()

    def sql_insert(self, table_name:str, columns:str, v_num:str, values:tuple) -> None:
        '''
        table_name = the name of the table
        columns = the columns(NAME,...) e.g: 'id,name,...'
        v_num = number of values e.g: '?,?,?,...'
        values = the values(1,...) e.g: (123,32,)
        '''
        self.cur.execute(f"INSERT INTO {table_name} ({columns}) VALUES ({v_num})",values)
        self.con.commit()
    
    def sql_show_all(self, table_name:str):
        '''
        table_name = the name of the table
        '''
        self.cur.execute(f"SELECT * FROM {table_name}")
        rows = self.cur.fetchall()
        print(self.data[table_name])
        for row in rows:
            print(row)
    
    def sql_update(self, table_name:str, column:str, new_value, condition_column:str, condition_value) -> None:
        '''
        table_name = the name of the table
        column = the name of the column we want to change a item of
        new_value = the new value for the changed item
        condition_column = the name of column the condition is on it
        condition_value = the value for condition
        '''
        self.cur.execute(f'UPDATE {table_name} set {column}="{new_value}" WHERE {condition_column}={condition_value}')
        self.con.commit()