from dotenv import load_dotenv
import os
import numpy as np

def db_info() -> list:
    
    load_dotenv()
    
    info = []

    info.append(os.getenv("USER_NAME"))
    info.append(os.getenv("PASSWORD"))
    info.append(os.getenv("HOST_NAME"))
    info.append(os.getenv("DB_NAME"))
    
    return info

def normal_distributions() -> list:
    
    age_normal = np.random.normal(45, 10, 10000)
    primary_salary_normal = np.random.normal(20000, 1000, 10000)
    secondary_salary_normal = np.random.normal(30000, 1000, 10000)
    tertiary_salary_normal = np.random.normal(60000, 1000, 10000)
    
    output = [age_normal, primary_salary_normal, secondary_salary_normal, tertiary_salary_normal]
    
    return output