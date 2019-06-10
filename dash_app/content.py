import os

import dash
import dash_html_components as html
import dash_core_components as dcc

list_of_images = []

def download_tab():
    
    coco_download = html.Div([
        dcc.Dropdown(
            id='coco_categories',
            options=[{'label': i, 'value': i} for i in ['airplane', 'bus']],
            value=[],
            multi=True
        ),
        html.Br(),
        dcc.RadioItems(
            id='coco_dataset',
            options=[{'label': i, 'value': i} for i in ['train', 'valid', 'all']],
            value=None,
            labelStyle={'display': 'inline-block'}
        ),
        html.Br(),
        html.Button(
            'Download',
            id='coco_download'
        ),
        html.Div(id='progress'),
    ], 
        className='block',
        style={
            'padding': '5%', 
            'width': '60%',
        }
    )
    path = '/home/paulina/Documents/studia/adpb/fastai/dash_app/COCO'
    if os.path.isdir(path):
        train_list = [path+'/train/'+i for i in os.listdir(path+'/train/')]
        valid_list = [path+'/valid/'+i for i in os.listdir(path+'/valid/')]
        list_of_images = train_list+valid_list
        
    coco_show = html.Div([
        dcc.Dropdown(
            id='image-dropdown',
            options=[{'label': i.split('/')[-1], 'value': i} for i in list_of_images],
            value=None),
        html.Div(id='show-coco-img'),
    ],
        style={'width': '80%'})
    
    return [html.Div(coco_download, style={'width': '50%', 'display': 'inline-block'}), html.Div(coco_show, style={'width': '50%', 'display': 'inline-block'})]
    
    
def model_tab():
    
    upload = html.Div([
        dcc.Upload(
            id='upload-data',
            children=html.Div([
                'Drag and Drop or ',
                html.A('Select File')
            ]),
            style={
                'width': '100%',
                'height': '60px',
                'lineHeight': '60px',
                'borderWidth': '1px',
                'borderStyle': 'dashed',
                'borderRadius': '5px',
                'textAlign': 'center',
                'margin': '10px'
            },
            # Allow multiple files to be uploaded
#             multiple=True
        ),
        html.Div(id='output-data-upload'),
    ])
    
    return upload

def video_tab():
    pass