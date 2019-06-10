import base64
from dash.dependencies import Input, Output, State
import dash_html_components as html

from os import path
import sys
sys.path.append(path.join(path.dirname(__file__), '..'))
    
from fastai.vision.data import COCO_download

from server import app
# from content import download_tab, model_tab, video_tab
    

@app.callback(Output('output-data-upload', 'children'),
              [Input('upload-data', 'contents')],
              [State('upload-data', 'filename'),
               State('upload-data', 'last_modified')])
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
#         children = [parse_contents(c, n, d) for c, n, d in zip(list_of_contents, list_of_names, list_of_dates)]

        return parse_contents(list_of_contents, list_of_names, list_of_dates)
    
def parse_contents(contents, filename, date):
    print(contents)
    return html.Div([
        html.H5(filename),
        html.Img(src=contents)
    ])


@app.callback(
    Output('progress', 'children'),
    [Input('coco_download', 'n_clicks')],
    [State('coco_categories', 'value'),
    State('coco_dataset', 'value')])
def download_coco(n_clicks, categories, dataset):
#     print(n_clicks, dataset)
    if n_clicks:
        COCO_download(dataset=dataset, category=categories)
        

@app.callback(
    Output('show-coco-img', 'children'),
    [Input('image-dropdown', 'value')])
def show_coco(value):
    if value:
        name = value.split('/')[-1]
        encoded_image = base64.b64encode(open(value, 'rb').read())
        pls = str(encoded_image)[2:-1]
        print('data:image/jpeg;base64,{}'.format(pls))
        return html.Div([
            html.H5(name),
            html.Img(src='data:image/jpeg;base64,{}'.format(pls))
        ])
    
