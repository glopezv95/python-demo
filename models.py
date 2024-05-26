from faker import Faker
import numpy as np
from datetime import datetime as dt
from tqdm import tqdm
import psycopg
from psycopg.sql import SQL, Literal

import data
import functions as funcs

class Table():
    
    user_name, password, host_name, db_name = funcs.db_info()
    conn = psycopg.connect(host=host_name, dbname=db_name, user=user_name, password=password)
    cur = conn.cursor()
    
    def __init__(self, name:str, cols:dict):
        
        self.user_name, self.password, self.host_name, self.db_name = funcs.db_info()
        self.cols = cols
        self.col_names = cols.keys()
        self.col_types = cols.values()
        self.name = name
        self.field_list = [key + ' ' + value for key, value in self.cols.items()]
    
    def connect(self):
        
        self.conn = psycopg.connect(
            host=self.host_name,
            dbname=self.db_name,
            user=self.user_name,
            password=self.password)
        
        self.cur = self.conn.cursor()
        
    def drop(self):
        
        query = SQL('DROP TABLE IF EXISTS {name}').format(name=SQL(self.name))
        return query
    
    def create_table(self):
        
        self.cur.execute(self.drop())
        
        query = SQL("CREATE TABLE {table} ({fields})").format(
            table = SQL(self.name),
            fields = SQL(', ').join(map(SQL, self.field_list))
        )
                                   
        self.cur.execute(query)
        
    def populate_row(self, values: tuple):
        
        query = SQL("INSERT INTO {table} ({fields}) VALUES ({values})").format(
            table = SQL(self.name),
            fields = SQL(', ').join(map(SQL, self.col_names)),
            values = SQL(', ').join(map(Literal, values))
        )       
                     
        self.cur.execute(query)
    
    def get(self, qselect:list, qfrom:str, qwhere:dict, qorderby:list, qlimit:int) -> list:
        
        where = [key + ' = ' + "'" + value + "'" for key, value in qwhere.items()]
        
        query= SQL("""
            SELECT {qselect}
            FROM {qfrom}
            WHERE {qwhere}
            ORDER BY {qorderby}
            LIMIT {qlimit}
            """).format(
                qselect = SQL(', ').join(map(SQL, qselect)),
                qfrom = SQL(qfrom),
                qwhere = SQL(' AND ').join(map(SQL, where)),
                qorderby = SQL(', ').join(map(SQL, qorderby)),
                qlimit = Literal(qlimit)
            )
          
        output_list = self.cur.execute(query).fetchall()
        
        return output_list
        
    def commit(self):
        self.conn.commit()
        
    def close(self):
        self.conn.close()
    
class PeopleTable(Table):
    
    def __init__(self,name: str, cols: dict, num_rows:int):
        super().__init__(name, cols)
        self.num_rows = int(num_rows)
    
    def create_row(
        self,
        fake:Faker,
        age_normal: np.array,
        primary_salary_normal: np.array,
        secondary_salary_normal: np.array,
        tertiary_salary_normal: np.array) -> tuple:

        gender = np.random.choice(data.GENDER, p=(0.48, 0.52))
                    
        if gender == 'male':
            name = fake.first_name_male()
        
        else:
            name = fake.first_name_female()
            
        lastname = fake.last_name()
        
        age = round(np.random.choice(age_normal))
        age = age if age >= 18 else 18
        age = age if age <= 65 else 65
        
        birth_province = np.random.choice(data.PROVINCES)
        studies = np.random.choice(data.STUDIES, p=(0.5, 0.4, 0.1))
        
        if studies == 'primary':
            partner = str(np.random.choice(data.PARTNER, p=(0.4, 0.6))).upper()
            salary = round(np.random.choice(primary_salary_normal), 2)
            salary = salary if salary >= 16000.00 else 16000.00
        
        elif studies == 'secondary':
            partner = str(np.random.choice(data.PARTNER, p=(0.1, 0.9))).upper()
            salary = round(np.random.choice(secondary_salary_normal), 2)
            salary = salary if salary >= 24000.00 else 24000.00
            
        else:
            partner = 'False'
            salary = round(np.random.choice(tertiary_salary_normal), 2)
            salary = salary if salary >= 30000.00 else 30000.00
        
        years_in_company = np.random.randint(1, age -16)
        remote_days = np.random.randint(0, 6)
        department = np.random.choice(data.DEPARTMENTS)
        input_date = dt.now()
        
        output = (
            name, lastname, gender, age, birth_province, studies, department,
            partner, salary, years_in_company, remote_days, input_date
        )
        
        return output
    
    def generate_data(self) -> list:

        fake = Faker()
        age_normal, primary_salary_normal, secondary_salary_normal, tertiary_salary_normal = \
            funcs.normal_distributions()
        
        data = [
            self.create_row(
                fake,
                age_normal,
                primary_salary_normal,
                secondary_salary_normal,
                tertiary_salary_normal) for _ in tqdm(range(self.num_rows), desc=f"{self.name.upper()} TABLE")
        ]
        
        return data
    
    def populate_copy(self):
        
        query = SQL("COPY people ({cols}) FROM STDIN").format(
            cols = SQL(', ').join(map(SQL, data.PEOPLE_DICT.keys()))
        )
        
        with self.cur.copy(query) as copy:
            for record in self.generate_data():
                copy.write_row(record)