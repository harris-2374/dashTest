import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app


body = dbc.Container(
    children=[
        dbc.Row(
            dbc.Col(
                id="col1",
                children=[
                    html.P("HELLO"),  
                ],
                width=12,
            )
        ),
    ],
    fluid=True
)


layout = html.Div([body])

