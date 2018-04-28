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

binance = exBinance()
kucoin = exKucoin()
bitfinex = exBitfinex()

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
            html.Th("Price (U$)"),
            html.Th("Bid (U$)"),
            html.Th("Ask (U$)"),
            ]
            )] +

        # Body
        [html.Tr([
            html.Td("Binance"),
            html.Td(binance.getPrice(), id="bin-price", style={"color":"blue"}),
            html.Td(binance.getBid(), id="binbid", style={"color":"blue"}),
            html.Td(binance.getAsk(), id="binask", style={"color":"blue"}),
            ]
        )] + 
        
        [html.Tr([
            html.Td("Kucoin"),
            html.Td(kucoin.getPrice(), id="kuk-price", style={"color":"blue"}),
            html.Td(kucoin.getBid(), id="kukbid", style={"color":"blue"}),
            html.Td(kucoin.getAsk(), id="kukask", style={"color":"blue"}),
            ]
        )] +
            
        [html.Tr([
            html.Td("Bitfinex"),
            html.Td(bitfinex.getPrice(), id="btf-price", style={"color":"blue"}),
            html.Td(bitfinex.getBid(), id="btfbid", style={"color":"blue"}),
            html.Td(bitfinex.getAsk(), id="btfask", style={"color":"blue"}),
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
        interval=7000
        ),
    
    #generate_table(df),
])

#   BINANCE

@app.callback(
    Output('bin-price', component_property='children'),
    events = [Event('field-update', 'interval')]
)
def update_bin():
    return binance.getPrice()

@app.callback(
    Output('binbid', component_property='children'),
    events = [Event('field-update', 'interval')]
)
def update_binbid():
   return binance.getBid()

@app.callback(
    Output('binask', component_property='children'),
    events = [Event('field-update', 'interval')]
)
def update_binask():
    return binance.getAsk()


#   KUCOIN

@app.callback(
    Output('kuk-price', component_property='children'),
    events = [Event('field-update', 'interval')]
)
def update_kuk():
    return kucoin.getPrice()
 
@app.callback(
    Output('kukbid', component_property='children'),
    events = [Event('field-update', 'interval')]
)
def update_kukbid():
    return kucoin.getBid()

 
@app.callback(
    Output('kukask', component_property='children'),
    events = [Event('field-update', 'interval')]
)
def update_kukask():
    return kucoin.getAsk()
 
 # BITFINEX 
   
@app.callback(
    Output('btf-price', component_property='children'),
    events = [Event('field-update', 'interval')]
)
def update_btf():
    return bitfinex.getPrice()
   
@app.callback(
    Output('btfbid', component_property='children'),
    events = [Event('field-update', 'interval')]
)
def update_btfbid():
    return bitfinex.getBid()
   
@app.callback(
    Output('btfask', component_property='children'),
    events = [Event('field-update', 'interval')]
)
def update_btfask():
    return bitfinex.getAsk()


if __name__ == '__main__':
    app.run_server(debug=True)