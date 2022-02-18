import psycopg2
import data_cleanse
import pandas as pd
from sqlalchemy import create_engine
import io

conn = psycopg2.connect("host=localhost dbname = POC user=postgres password = ****")

conn.autocommit = True
cur = conn.cursor()

# cur.execute("""
#     CREATE TABLE energy_consumption(
        
#         iso_code varchar(10),
#         country varchar(50),
#         year int,
#         population float,
#         gdp float,
#         coal_consumption float,
#         coal_production float,
#         coal_electricity float,
#         gas_electricity float,
#         hydro_electricity float,
#         nuclear_electricity float,
#         oil_electricity float,
#         oil_production float,
#         oil_consumption float,
#         solar_electricity float,
#         wind_electricity float,
#         gas_consumption float,
#         gas_production float,
#         hydro_consumption float,
#         nuclear_consumption float,
#         solar_consumption float,
#         wind_consumption float
#         )""")

# cur.execute("""
#     CREATE TABLE country_iso(
#         iso_code varchar(10),
#         country varchar(50))""")

# conn.commit()

#df = pd.read_csv("clean_data.csv")

df_countries = data_cleanse.iso_code_u
df = data_cleanse.df_2

engine = create_engine("postgresql+psycopg2://postgres:****@localhost:5432/POC")

df_countries.to_sql('country_iso', engine, if_exists='replace')

df.to_sql('energy_consumption', engine, if_exists='replace')
