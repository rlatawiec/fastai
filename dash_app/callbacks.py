import base64
from dash.dependencies import Input, Output, State
import dash_html_components as html

from server import app
from content import img_tab, model_tab, video_tab
    

@app.callback(Output('output-data-upload', 'children'),
              [Input('upload-data', 'contents')],
              [State('upload-data', 'filename'),
               State('upload-data', 'last_modified')])
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
#         children = [parse_contents(c, n, d) for c, n, d in zip(list_of_contents, list_of_names, list_of_dates)]

        return parse_contents(list_of_contents, list_of_names, list_of_dates)
    
def parse_contents(contents, filename, date):
#     content_type, content_string = contents.split(',')
#     decoded = base64.b64decode(content_string)
    
    return html.Div([
        html.H5(filename),
#         html.Img(src='data:image/png;base64,{}'.format(decoded)),
        html.Img(src=contents)
    ])