# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, Event
from main import *

import pandas as pd

d = {'Binance': ['askb', 'bidb'], 'Kucoin': ['askb', 'bidb']}
df = pd.DataFrame(data=d)

app = dash.Dash()

app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([
            html.Th(col) for col in dataframe.columns]
        )] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )
    
def generate_table2():
    return html.Table(
        # Header
        [html.Tr([
            html.Th("Exchange"),
            html.Th("Price"),
            html.Th("Bid"),
            html.Th("Ask"),
            ]
            )] +

        # Body
        [html.Tr([
            html.Td("Binance"),
            html.Td(exBinance().getPrice(), id="bin-price"),
            html.Td("BinanceBid"),
            html.Td("BinanceAsk"),
            ]
        )] + 
        
        [html.Tr([
            html.Td("Kucoin"),
            html.Td("price"),
            html.Td("Bid"),
            html.Td("Ask"),
            ]
        )]
    
    )

app.layout = html.Div(children=[
    html.H1(children='Bitcoin Exanges Prices Chart'),
    
    html.Div(children='''
        Dash: A web application framework for Python.
    '''),
    
    #html.H1(
    #    "U$ {}".format(exBinance().getPrice()),
    #    id='live-field'
    #    ),
    
    generate_table2(),
    
    dcc.Interval(
        id='field-update', 
        interval=5000
        ),
    
    #generate_table(df),
])

@app.callback(
    Output('bin-price', component_property='children'),
    events = [Event('field-update', 'interval')]
)
def update_output_div():
    price = exBinance().getPrice()
    return 'U$ {}'.format(price)

if __name__ == '__main__':
    app.run_server(debug=True)