import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from app import app

body = dbc.Container(
        children=[
            
        ],
    fluid=True,
    key='home_container',
    )

layout = html.Div([
            body
        ])
