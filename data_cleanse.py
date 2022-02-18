import pandas as pd
import numpy as np

#Loading kaggle dataset
energy = pd.read_csv("world_energy_consumption.csv")

#Creating subset of desired columns
data = energy.filter(["iso_code","country","year","population","gdp","coal_consumption","coal_production","coal_electricity","gas_electricity","hydro_electricity","nuclear_electricity","oil_electricity","oil_production","oil_consumption","solar_electricity","wind_electricity","gas_consumption","gas_production","hydro_consumption","nuclear_consumption","solar_consumption","wind_consumption"],axis=1)
data_prof = energy.filter(["iso_code","country","year","population","gdp","coal_consumption","coal_production","coal_electricity","gas_electricity","hydro_electricity","nuclear_electricity","oil_electricity","oil_production","oil_consumption","solar_electricity","wind_electricity","gas_consumption","gas_production","hydro_consumption","nuclear_consumption","solar_consumption","wind_consumption"],axis=1)

#Data profiing, look at null values, as well as column statisticss
print(data_prof.describe())
data_prof.isnull().sum(axis=0)

#Next we want to drop the rows that don't contain iso_code's
country_data = data.dropna(subset=['iso_code'])

#Create second table including iso_codes and country names
iso_code = pd.DataFrame(country_data,columns=['iso_code','country'])
iso_code_u = iso_code.drop_duplicates()
iso_code_u = iso_code_u.set_index('iso_code')



#Don't need this step, but leaving in for now.
df = country_data.fillna(0)

#Ask pandas to convert the object types to it's best guess, which was strings
df_2 = df.convert_dtypes()\

#Removes the pandas index and replaces with the iso_code column
df_2 = df_2.set_index('iso_code')




