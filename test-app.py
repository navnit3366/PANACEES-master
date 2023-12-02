#!/bin/env python3

# Example from https://dash.plot.ly/getting-started

import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#000000',
    'text': '#0fffff'
}

app.layout = html.Div(children=[
    html.H1(
        children='Hello from Dash',
        style={
            'textAlign': 'right',
            'color': colors['text']
        }
    ),

    html.Div(children='''Dash: A web application framework for Python.'''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 2, 7], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 8, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization',
                'font': dict(family="Droid Sans", size=22, color=colors['text']),
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background']
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
