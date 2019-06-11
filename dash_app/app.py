# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

import callbacks
from content import download_tab, model_tab, video_tab
from server import app

app.layout = html.Div(children=[
    html.Div([
        html.Span("fast.ai visualisation tool", className='app-title')
    ], className="row header"),
    
    html.Div([
            dcc.Tabs(
                id="tabs",
                style={"height":"20","verticalAlign":"middle"},
                children=[
                    dcc.Tab(label="Download dataset", value="download_tab"),
                    dcc.Tab(label="Model - Img", value="model_tab"),
                    dcc.Tab(label="Model - Video", value="video_tab"),
                ],
                value="download_tab",
            )
    ], className="tabs_div"
    ),
    html.Div(id="tab_content", 
             className="content", 
             style={}),
    
])

@app.callback(Output("tab_content", "children"), [Input("tabs", "value")])
def display_page(tab):
    if tab == "download_tab":
        return download_tab()
    elif tab == "model_tab":
        return model_tab()
    elif tab == "video_tab":
        return video_tab()
    
if __name__ == '__main__':
    app.run_server(debug=True, port=8123)
