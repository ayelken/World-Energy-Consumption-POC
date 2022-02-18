import pandas as pd
import matplotlib as plt
import seaborn as sns
import plotly as plot
import psycopg2
pd.options.plotting.backend = "plotly"
import plotly.graph_objects as go


#Create a conneciton to our database and query it for a new dataframe to download to csv for use in visualizations
conn = psycopg2.connect("host=localhost dbname = POC user=postgres password = ****")

cur = conn.cursor()

#visualization query
cur.execute("""SELECT iso_code, country, year, population, gdp, oil_consumption FROM energy_consumption where year > 1980""")

query_results = cur.fetchall()

#visualization dataframe creation from query results
df = pd.DataFrame(query_results, columns=['Iso_Code','Country','Year','Population','GDP','Oil_Consumption'])

#save new dataframe to csv for use in tableau
df.to_csv('wec_viz.csv')



#Plotly interactive map visual
# fig = go.Figure(data=go.Choropleth(
#     locations = df['Iso_Code'],
#     z = df['GDP'],
#     text = df['Country'],
#     colorscale = 'Blues',
#     autocolorscale = False,
#     marker_line_color='darkgray',
#     marker_line_width=0.5,
#     colorbar_tickprefix = '$'
# ))

# fig.show()
