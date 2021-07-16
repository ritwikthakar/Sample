import dash
import dash_html_components as html
import pandas as pd
import dash_bootstrap_components as dbc
import numpy as np
import FundamentalAnalysis as fa
from config import k
ticker = 'AAPL'


Income_Statement = fa.income_statement(ticker, k, period="annual")
Balance_Sheet = fa.balance_sheet_statement(ticker, k, period="annual")
Cash_Flow_Statement = fa.cash_flow_statement(ticker, k, period="annual")

def generate_table(dataframe, max_rows=45):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

app.layout = html.Div(children=[
    html.H4(children='Microsoft Balance Sheet'),
    generate_table(Balance_Sheet)
])

