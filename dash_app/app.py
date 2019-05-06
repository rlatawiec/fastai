# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

import callbacks
from content import img_tab, model_tab, video_tab
from server import app

app.layout = html.Div(children=[
    html.Div([
        html.Span("App - img visualisation", className='app-title')
    ], className="row header"),
    
    html.Div([
            dcc.Tabs(
                id="tabs",
                style={"height":"20","verticalAlign":"middle"},
                children=[
                    dcc.Tab(label="Img visualisation", value="img_tab"),
                    dcc.Tab(label="Model", value="model_tab"),
                    dcc.Tab(label="Video", value="video_tab"),
                ],
                value="img_tab",
            )
    ], className="row tabs_div"
    ),
    html.Div(id="tab_content", className="row", style={"margin": "2% 3%"}),
    
])

@app.callback(Output("tab_content", "children"), [Input("tabs", "value")])
def display_page(tab):
    if tab == "img_tab":
        return img_tab()
    elif tab == "model_tab":
        return model_tab()
    elif tab == "video_tab":
        return video_tab()
    
if __name__ == '__main__':
    app.run_server(debug=True)