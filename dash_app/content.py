import dash
import dash_html_components as html
import dash_core_components as dcc

list_of_images = ['a', 'b', 'c']

def img_tab():
    return html.Div([
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
#         dcc.Dropdown(
#             id='image-dropdown',
#             options=[{'label': i, 'value': i} for i in list_of_images],
#             value=list_of_images[0]
#         ),
        html.Div(id='output-data-upload'),
    ])
    
    
def model_tab():
    pass

def video_tab():
    pass