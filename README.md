# PYTHON PRACTISE

![alt tag](https://realpython.com/learn/python-first-steps/images/pythonlogo.jpg)

### KIRAN REDDY KANCHARLA

### kiran.kancharla92@gmail.com



from __future__ import print_function
import sys, re
from pyspark.sql import SparkSession,HiveContext
import pyspark.sql.functions as f
from pyspark.sql.types import *
from pyspark.sql import DataFrameStatFunctions as statFunc
import subprocess
from pyspark.sql import Window
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as ff




traces = []

client_data.bin = pd.to_numeric(client_data.bin)

bins = [int(i) for i in client_data.bin.unique()]
bins = list(np.sort(bins))

for bin_no in bins:
  new_data = client_data.loc[(client_data.bin == bin_no)]
  trace = go.Bar(
    y=[int(i) for i in list(new_data.dfiference)],
    x=[int(i) for i in list(new_data.client_identifier)],
    visible = False,
    name='Difference at bin' + ' ' + str(bin_no),
    marker = dict(color = 'green'),
    xaxis='x2', yaxis='y2',
    width = 3,
  )
  traces.append(trace)

for bin_no in bins:
  new_data = df_data.loc[(df_data.Bin == bin_no)]
  trace1 = {"x": list(new_data.Bin), 
          "y": [int(i) for i in list(new_data.Predicted)], 
          "marker": {"color": "yellow", "size": 12}, 
          "mode": "markers", 
          "name": "Bin" + ' ' + str(bin_no), 
          "type": "scatter",
           }
  traces.append(trace1)


# Make traces for graph
trace1 = go.Scatter(
    y=[int(i) for i in list(df_data.Predicted)],
    x=list(df_data.Bin),
    visible = True,
    name='Predicted Cumulative sum',
    marker = dict(color = 'green'),
    )
traces.append(trace1)
        
trace2 = go.Scatter(
    y=[int(i) for i in list(df_data.actual_cumsum)],
    x=list(df_data.Bin),
    visible = True,
    name='Actual Cumulative sum',
    marker = dict(color = 'blue'),
    )
traces.append(trace2)
  
  
trace3 = go.Scatter(
    y=[int(i) for i in list(df_data.Red_1)],
    x=list(df_data.Bin),
    visible = True,
    name='Red Alert cumsum',
    marker = dict(color = 'red'),
    )
traces.append(trace3)  


traces.append(trace3)

clients = df_data_client.client_identifier.unique()
clients.sort()

clients = [int(i) for i in range(len(clients))]

df_data_client.client_identifier = pd.to_numeric(df_data_client.client_identifier)


for client in clients:
  new_data = df_data_client.loc[(df_data_client.client_identifier == client)]
  trace3 = go.Scatter(
      y=list(new_data.Predicted),
      x=list(new_data.Bin),
      name='Predicted Cumsum',
      visible=False,
      marker = dict(
          color = 'green',
          line = dict(
              color = 'rgba(68, 71, 80, 1.0)',
              width = 1)
      ),
      xaxis='x3', yaxis='y3',
  )
  traces.append(trace3)

  trace4 = go.Scatter(
      y=list(new_data.actual_cumsum),
      x=list(new_data.Bin),
      name='Actual Cumsum',
      visible=False,
      marker = dict(
          color = 'blue',
          line = dict(
              color = 'rgba(68, 71, 80, 1.0)',
              width = 1)
      ),
      xaxis='x3', yaxis='y3',
  )
  traces.append(trace4)
  
  trace5 = go.Scatter(
      y=list(new_data.Red_1),
      x=list(new_data.Bin),
      name='<b>Red Alert Cumsum<b>',
      visible=False,
      marker = dict(
          color = 'red',
          line = dict(
              color = 'rgba(68, 71, 80, 1.0)',
              width = 1)
      ),
      xaxis='x3', yaxis='y3',
  )
  traces.append(trace5)

  
# Add trace data to figure
#figure.extend(go.Data([trace1, trace2,trace3]))
data = traces



layout = go.Layout(
    barmode='stack',
    title = "<b>Cumulative sum graph for date <b>" + ' ' + str(date),
    font=dict(family='Times New Roman', size=16, color='black'),
    paper_bgcolor='darkgrey',
    plot_bgcolor='white',
    xaxis=dict(
        domain=[0, 0.5],
        title='<b>\n\n\n\n\n\nBin Number<b>',
        autotick=False,
        ticks='outside',
        nticks=37,
        tick0 = 961,
        tickwidth=5,
        range=[961,1141],
        ticklen=22,
        dtick = 5,
        color = 'black',
    ),
    yaxis=dict(
        title='<b>Cumulative sum<b>',
        domain=[0.5, 1],
        autotick=True,
        ticks='outside',
        tick0=0,
        dtick= 100,
        ticklen=22,
        tickwidth=5,
        color = 'black',
    ),
    xaxis2=dict(
        domain=[0.65, 1],
        title='<b>\n\n\n\n\n\nBin Number<b>',
        autotick=False,
        ticks='outside',
        tick0=961,
        dtick= 5,
        ticklen=37,
        tickwidth=2,
        color = 'black',
    ),
    yaxis2 = dict(
        title='<b>Volume difference for client<b>',
        domain=[0.5, 1],
        anchor='x2',
        autotick=True,
        ticks='outside',
        tick0=0,
        dtick= 1,
        ticklen=20,
        tickwidth=5,
        color = 'black',
    ),
    xaxis3=dict(
        domain=[0, 0.5],
        title='<b>\n\n\n\n\n\nBin Number<b>',
        autotick=False,
        ticks='outside',
        nticks=37,
        tick0 = 961,
        tickwidth=5,
        range=[961,1141],
        ticklen=22,
        dtick = 5,
        color = 'black',
    ),
    yaxis3=dict(
        title='<b>Cumulative sum<b>',
        domain=[0, 0.4],
        autotick=True,
        ticks='outside',
        tick0=0,
        dtick= 100,
        ticklen=22,
        tickwidth=5,
        color = 'black',
    ),
)


def filter_menu(client):
    length = 2 * len(bins) + 3 + 82
    a = list(np.array([False] * length))
    a[client] = True
    for i in range(len(bins),2*len(bins)):
      a[i] = True
    a[-1],a[-2],a[-3] = True,True,True
    return list(a)

def func():
    length = 2 * len(bins) + 3 + 82
    a = list(np.array([False] * length))
    for i in range(len(bins),2*len(bins)):
      a[i] = True
    a[-1],a[-2],a[-3] = True,True,True
    return list(a)

def client_menu(client):
    length = 2 * len(bins) + 3 + 82
    a = list(np.array([False] * length))
    for i in range(2*len(bins)):
      a[i] = True
    a[client] = True
    return list(a)

def client_func():
    length = 2 * len(bins) + 3 + 82
    a = list(np.array([False] * length))
    for i in range(2*len(bins)):
      a[i] = True
    return list(a)

  
updatemenus=list([
dict(
yanchor='top',
showactive = True,
active = -1,
direction = 'down',
buttons=list([
dict(
  args=['visible', func()],
  label= "Select Bin",
  method='restyle'
  )]) + list([
dict(
  args=['visible', filter_menu(client)],
  label= "bin" + ' ' + str(bins[client]),
  method='restyle'
  )for client in range(len(bins))]),
  pad = {'r': 10, 't': 10},
  x = 0.1,
  xanchor = 'left',
  y = 1.1,
),
dict(
yanchor='top',
showactive = True,
active = -1,
direction = 'down',
buttons=list([
dict(
  args=['visible', client_func()],
  label= "Select client",
  method='restyle'
  )]) + list([
dict(
  args=['visible', client_menu(client)],
  label= "bin" + ' ' + str(bins[client]),
  method='restyle'
  )for client in range(len(clients))]),
  pad = {'r': 10, 't': 10},
  x = 0.1,
  xanchor = 'left',
  y = 0,
)
])



layout['updatemenus'] = updatemenus

layout.annotations = list([
    dict(text='Select Bin:', x=0.1, y=1.085,align = 'left', showarrow=False)
])
  

# Plot!
figure = go.Figure(data=data, layout=layout)
plotly.offline.plot(figure, filename='subplot_table')
