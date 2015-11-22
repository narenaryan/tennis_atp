from random import shuffle
import colorsys
import pandas as pd
from plotly.offline import  init_notebook_mode, iplot
from plotly.graph_objs import *

init_notebook_mode()

# Load players into players dataframe 
players = pd.read_csv('atp_players.csv')

# Find top 20 countries with more player frequncies 
countries = players.groupby(['Country']).size()
selected_countries = countries.sort_values(ascending=False)[:20]

# Generating 20 random color palettes for plotting each country.
N = 20
HSV_tuples = [(x*1.0/N, 0.5, 0.5) for x in range(N)]
RGB_tuples = map(lambda x: colorsys.hsv_to_rgb(*x), HSV_tuples)
shuffle(RGB_tuples)

""" Plot.ly plotting code. A plot.ly iplot needs data and a layout 
    So now we prepare data and then layout. Here data is a scatter plot
"""
trace0 = Scatter(
    x = list(selected_countries.index),
    y = list(selected_countries.values),
    mode = 'markers',
    marker = {'color' : plot_colors, 'size' : [30] * N}
)

# Data can be a list of plot types. You can have more than one scatter plots on figure 

data = [trace0]

# layout has properties like x-axis label, y-axis label, background-color etc

layout = Layout(
    xaxis = {'title':"Country"},
    yaxis = {'title':" No of players produced"},
    showlegend=False,
    height=600,
    width=600,
    paper_bgcolor='rgb(233,233,233)',  # set paper (outside plot) 
    plot_bgcolor='rgb(233,233,233)', 
)

# Build figure from data and layout and plot it.
fig = Figure(data=data, layout=layout)
iplot(fig)