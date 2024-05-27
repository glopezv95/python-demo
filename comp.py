import tables
import data
from tqdm import tqdm
import numpy as np
from datetime import datetime as dt
    
def compute(name:str):
    
    if name == 'people':
        
        num_rows = input('Please select number of rows for the people table: ')
        print()
        
        table = tables.PeopleTable(
            name = 'people',
            cols = data.PEOPLE_DICT,
            num_rows = num_rows
        )

        table.connect()
        table.create_table()
        table.populate_copy()
        
    elif name == 'ccaa':
        
        table = tables.Table(
            name=name,
            cols=data.CCAA_DICT
        )
        
        table.connect()
        table.create_table()
        
        for ccaa in tqdm(data.CCAA_JSON.keys(), desc = f'{name.upper()} TABLE'):
            
            info = (ccaa, data.CCAA_JSON[ccaa]['código autonómico'])
            table.populate_row(info)
    
    elif name == 'provinces':
    
        table = tables.Table(
            name = name,
            cols = data.PROVINCE_DICT
        )
        
        table.connect()
        table.create_table()
        
        for ccaa in tqdm(data.CCAA_JSON.keys(), desc = f'{name.upper()} TABLE'):
            for i, province in enumerate(data.CCAA_JSON[ccaa]['provincias']):
                
                info = (
                    data.CCAA_JSON[ccaa]['código autonómico'],
                    province,
                    data.CCAA_JSON[ccaa]['códigos ISO'][i])
                
                table.populate_row(info)
    
    elif name == 'departments':
        
        table = tables.Table(
            name = name,
            cols = data.DEPARTMENTS_DICT
        )
        
        table.connect()
        table.create_table()
        
        for department in tqdm(data.DEPARTMENTS, desc = f'{name.upper()} TABLE'):
            
            created = np.random.randint(2000, dt.today().year)
            directors = table.get(
                qselect=['name, lastname'],
                qfrom = 'people',
                qwhere = {'department': department},
                qorderby = ['salary'],
                qlimit = 3
            )

            director = directors[np.random.randint(0, len(directors))]
            director_name = director[0] + ' ' + director[1]
            email = str(director[0][0] + director[1] + '@gabsa.com').lower()
            info = (department, created, director_name, email)
            
            table.populate_row(values = info)
            
    elif name == 'projects':
        
        table = tables.Table(
            name = name,
            cols = data.PROJECTS_DICT
        )
        
        table.connect()
        table.create_table()
        year_list = range(2000, dt.today().year +1)
        
        for project in tqdm(data.PROJECTS, desc=f'{name.upper()} TABLE'):
        
            department = list(np.random.choice(data.DEPARTMENTS, np.random.randint(1, 5), replace=False))
            year = int(np.random.choice(year_list))
            budget = round(np.random.normal(50000, 5000, 1000)[0], 2)
            budget = budget if budget >= 1000.00 else 1000.00
            
            info = (project, year, department, budget)
            table.populate_row(values = info)
    
    table.commit()
    table.close()
    print()