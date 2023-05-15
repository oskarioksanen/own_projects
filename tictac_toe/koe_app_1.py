import dash
from dash import Dash, html, dcc, callback, Output, Input, ctx
import plotly.express as px
import pandas as pd

marks = {"x": "X",
         "y": "Y"}

app = Dash(__name__)

app.layout = html.Div(
    style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center', 'height': '100vh'},
    children=[
        html.Div(
            [
                html.H1('Kokeilu', style={'textAlign':'center', 'fontSize': '36px', 'fontFamily': 'Arial'}),
                html.H2(id='player_turn', children='-------', style={'textAlign': 'center', 'fontSize': '20px', 'fontFamily': 'Calibri'}),
                html.Div(
                    [
                        dcc.Store(id='text_1_1', data=''),
                        dcc.Store(id='text_1_2', data=''),
                        dcc.Store(id='text_1_3', data=''),
                        html.Button('Button 1', id='btn_1_1', n_clicks=0, style={'width': '100px', 'height': '100px', 'border-radius': '0'}),
                        html.Button('Button 2', id='btn_1_2', n_clicks=0, style={'width': '100px', 'height': '100px', 'border-radius': '0'}),
                        html.Button('Button 3', id='btn_1_3', n_clicks=0, style={'width': '100px', 'height': '100px', 'border-radius': '0'})
                    ],
                    className='grid_row'),
                html.Div(
                        [
                            dcc.Store(id='text_2_1', data=''),
                            dcc.Store(id='text_2_2', data=''),
                            dcc.Store(id='text_2_3', data=''),
                            html.Button('Button 1', id='btn_2_1', n_clicks=0, style={'width': '100px', 'height': '100px', 'border-radius': '0'}),
                            html.Button('Button 2', id='btn_2_2', n_clicks=0, style={'width': '100px', 'height': '100px', 'border-radius': '0'}),
                            html.Button('Button 3', id='btn_2_3', n_clicks=0, style={'width': '100px', 'height': '100px', 'border-radius': '0'})
                        ],
                        className='grid_row'),
                html.Div(
                        [
                            dcc.Store(id='text_3_1', data=''),
                            dcc.Store(id='text_3_2', data=''),
                            dcc.Store(id='text_3_3', data=''),
                            html.Button('Button 1', id='btn_3_1', n_clicks=0, style={'width': '100px', 'height': '100px', 'border-radius': '0'}),
                            html.Button('Button 2', id='btn_3_2', n_clicks=0, style={'width': '100px', 'height': '100px', 'border-radius': '0'}),
                            html.Button('Button 3', id='btn_3_3', n_clicks=0, style={'width': '100px', 'height': '100px', 'border-radius': '0'})
                        ],
                        className='grid_row'),
                html.Button('Clear Button', id='clear_button', n_clicks=0),
                html.H3(id='result', children='Alkuteksti', style={'textAlign': 'center', 'fontSize': '16px', 'fontFamily': 'Calibri'})
            ])
    ])

def calculate_clicks(btns):
    sum = 0
    for n_click in btns:
        sum += n_click
    return sum

"""@callback(
    Output('btn_1_1', 'children'),
    Output('btn_1_2', 'children'),
    Output('btn_1_3', 'children'),
    Output('btn_2_1', 'children'),
    Output('btn_2_2', 'children'),
    Output('btn_2_3', 'children'),
    Output('btn_3_1', 'children'),
    Output('btn_3_2', 'children'),
    Output('btn_3_3', 'children'),
    Input('clear_button', 'n_clicks')
)
def clear_graph(n_clicks):

    outputs = []
    for i in range(9):
        mark = ""
        outputs.append(mark)

    return tuple(outputs)"""


@callback(
    [Output('btn_1_1', 'children'),
    Output('btn_1_2', 'children'),
    Output('btn_1_3', 'children'),
    Output('btn_2_1', 'children'),
    Output('btn_2_2', 'children'),
    Output('btn_2_3', 'children'),
    Output('btn_3_1', 'children'),
    Output('btn_3_2', 'children'),
    Output('btn_3_3', 'children'),
    Output('result', 'children'),
    Output('player_turn', 'children')],
    [Input('text_1_1', 'data'),
    Input('text_1_2', 'data'),
    Input('text_1_3', 'data'),
    Input('text_2_1', 'data'),
    Input('text_2_2', 'data'),
    Input('text_2_3', 'data'),
    Input('text_3_1', 'data'),
    Input('text_3_2', 'data'),
    Input('text_3_3', 'data')],
    prevent_initial_call=True
)
def update_graph(data_1_1, data_1_2, data_1_3,
                 data_2_1, data_2_2, data_2_3,
                 data_3_1, data_3_2, data_3_3):

    board = [data_1_1, data_1_2, data_1_3,
             data_2_1, data_2_2, data_2_3,
             data_3_1, data_3_2, data_3_3]
    total_clicks = 0
    for mark in board:
        if mark != "":
            total_clicks += 1

    player = marks["x"] if total_clicks % 2 != 0 else marks["y"]
    next_turn = "Next up: "
    next_turn += marks["y"] if total_clicks % 2 != 0 else marks["x"]
    game_over = check_winner(board, player)
    teksti = "Ei voittajaa vielä"
    if game_over:
        teksti = "VOITTO!"
        next_turn = "-------"
        print(teksti)

    btns = [data_1_1, data_1_2, data_1_3,
            data_2_1, data_2_2, data_2_3,
            data_3_1, data_3_2, data_3_3]
    outputs = []
    for i, btn in enumerate(btns):
        mark = btn
        outputs.append(mark)

    return outputs + [teksti] + [next_turn]

@callback(
    Output('text_1_1', 'data'),
    Output('text_1_2', 'data'),
    Output('text_1_3', 'data'),
    Output('text_2_1', 'data'),
    Output('text_2_2', 'data'),
    Output('text_2_3', 'data'),
    Output('text_3_1', 'data'),
    Output('text_3_2', 'data'),
    Output('text_3_3', 'data'),
    Input('btn_1_1', 'n_clicks'),
    Input('btn_1_2', 'n_clicks'),
    Input('btn_1_3', 'n_clicks'),
    Input('btn_2_1', 'n_clicks'),
    Input('btn_2_2', 'n_clicks'),
    Input('btn_2_3', 'n_clicks'),
    Input('btn_3_1', 'n_clicks'),
    Input('btn_3_2', 'n_clicks'),
    Input('btn_3_3', 'n_clicks'),
    Input('text_1_1', 'data'),
    Input('text_1_2', 'data'),
    Input('text_1_3', 'data'),
    Input('text_2_1', 'data'),
    Input('text_2_2', 'data'),
    Input('text_2_3', 'data'),
    Input('text_3_1', 'data'),
    Input('text_3_2', 'data'),
    Input('text_3_3', 'data')
    #Input('dropdown-selection', 'value')
)
def update_values(n_btn_1_1, n_btn_1_2, n_btn_1_3,
                 n_btn_2_1, n_btn_2_2, n_btn_2_3,
                 n_btn_3_1, n_btn_3_2, n_btn_3_3,
                 mark_1_1, mark_1_2, mark_1_3,
                 mark_2_1, mark_2_2, mark_2_3,
                 mark_3_1, mark_3_2, mark_3_3):

    button_id = ctx.triggered_id if not None else 'No clicks yet'

    total_clicks = calculate_clicks([n_btn_1_1, n_btn_1_2, n_btn_1_3,
                                     n_btn_2_1, n_btn_2_2, n_btn_2_3,
                                     n_btn_3_1, n_btn_3_2, n_btn_3_3])


    player = marks["x"] if total_clicks % 2 != 0 else marks["y"]
    btns = ["btn_1_1", "btn_1_2", "btn_1_3",
            "btn_2_1", "btn_2_2", "btn_2_3",
            "btn_3_1", "btn_3_2", "btn_3_3"]
    btn_marks = [mark_1_1, mark_1_2, mark_1_3,
                 mark_2_1, mark_2_2, mark_2_3,
                 mark_3_1, mark_3_2, mark_3_3]
    outputs = []
    for i, btn in enumerate(btns):
        mark = ""
        if btn_marks[i] != '':
            mark = btn_marks[i]
        elif btn == button_id:
            mark = player
        outputs.append(mark)

    return tuple(outputs)

def check_winner(board, player):
    print("Board:")
    print(board)
    print("Player:")
    print(player)
    # Check rows
    for i in range(3):
        if board[i * 3] == board[i * 3 + 1] == board[i * 3 + 2] == player:
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == player:
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

app.run_server(debug=True)