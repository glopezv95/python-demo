<style>
    body { text-align: justify; }
    ul { padding-left: 2rem }
    li { list-style: none; }
</style>
# PostgreSQL - python company data project
This is a python project that generates a *PostgreSQL* database using `python`'s `psycopg` package and populates it using, among other, tools, `python`'s `numpy` package.

The **database** generated contains the following tables:
- **people**: This table contains demographic data (name, lastname, gender, age, birth_province, studies, department, partner, salary, years_in_company, remote_days, input_date).
- **ccaa**: This table contains each of Spain's Autonomous Communities and their respective ISO code.
- **provinces**: This table contains each of Spain's provinces with their respective Autonomous Community and ISO code.
- **departments**: This table stores data of 25 company departments (name, year created, director and contact email).
- **projects**: This table stores data of 50 company projects (name, year of each project instance, list of departments involved and related budget).
    
## Settings and configuration
### Virtual environment configuration
Generate the virtual environment with `pip`.
```
python -m venv venv
```
Activate the virtual environment in *Windows Powershell*.
```
venv/scripts/activate
```
or activate the virtual environment in `bash`.
```
source venv/bin/activate
```
### Install required packages with pip
```
pip install -r requirements.txt
```
### Set up .env and .gitignore
Create a `.env` file in the root directory that contains all the information related to the *PostgreSQL* database. This should be the structure of the `.env` file:
```
USER_NAME="some_user"
PASSWORD="some_password"
HOST_NAME="some_host"
DB_NAME="some_dbname"
```
Create a `.gitignore` file in the root directory that contains all files and directories not to be added and/or committed to git. This should be the structure of the `.gitignore` file:
```
venv
.env
__pycache__
```
## Program structure
### `models.py`
This script contains;
- the parent Class `Table`. This class contains attributes that describe the tables, as well as functions to drop, generate, populate and commit them to the database.

- the child class `PeopleTable`. This subclass contains specific logic to adecuately handle the `people` table. This includes asking the user for its length, as well as some additional logic to generate random data, copy it and use it to populate the `people` table inside the database.
### `secondary.py`
This script stores the function `compute`, which creates tables generating classes from the `models.py` applying the logic needed on each table for it to be properly generated and populated.
### `data.py`
This script contains variables that store miscellaneous information needed to generate the tables. This includes, among others, a json file containing Spain's Autonomous Communities and their respective Provinces, as well as dictionaries containing the fields of each table as keys and their SQL types as values.
### `main.py`
This script generates the database when run, creating instances of the `compute` function for each table in the database and formatting the style of the output.
## Input and output
With the virtual environment generated and all the necessary packages installed, the database can be generated by running `main.py`.
```
python main.py
```
Once the program starts running, it will ask for the desired length of the `people`'s table. Once this input is given, the program establishes the connection to the database, generates all the tables, populates them and closes the connection. The following is an example shell output when generating 500.000 rows in the peoples data.
```
(venv) PS C:...\Proyectos\postgresql\company> python main.py
-----------------------
Please select number of rows for the people table: 500000

PEOPLE TABLE: 100%|██████████████████████████████| 500000/500000 [01:21<00:00, 6126.65it/s]

CCAA TABLE: 100%|████████████████████████████████| 17/17 [00:00<00:00, 5666.18it/s]

PROVINCES TABLE: 100%|███████████████████████████| 17/17 [00:00<00:00, 2421.82it/s] 

DEPARTMENTS TABLE: 100%|█████████████████████████| 25/25 [00:01<00:00, 19.10it/s] 

PROJECTS TABLE: 100%|████████████████████████████| 50/50 [00:00<00:00, 3523.56it/s] 

Database generated successfully.
```