import dash
from dash import html
from dash.dependencies import Input, Output

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the grid layout
layout = html.Div(
    [
        html.Button(id="square-1", n_clicks=0, children="Square 1"),
        html.Button(id="square-2", n_clicks=0, children="Square 2"),
        html.Button(id="square-3", n_clicks=0, children="Square 3"),
        html.Button(id="square-4", n_clicks=0, children="Square 4"),
        html.Button(id="square-5", n_clicks=0, children="Square 5"),
        html.Button(id="square-6", n_clicks=0, children="Square 6"),
        html.Button(id="square-7", n_clicks=0, children="Square 7"),
        html.Button(id="square-8", n_clicks=0, children="Square 8"),
        html.Button(id="square-9", n_clicks=0, children="Square 9"),
    ],
    className="grid-container"
)

# Define the callback to handle button clicks
@app.callback(Output("square-1", "children"),
              Output("square-2", "children"),
              Output("square-3", "children"),
              Output("square-4", "children"),
              Output("square-5", "children"),
              Output("square-6", "children"),
              Output("square-7", "children"),
              Output("square-8", "children"),
              Output("square-9", "children"),
              Input("square-1", "n_clicks"),
              Input("square-2", "n_clicks"),
              Input("square-3", "n_clicks"),
              Input("square-4", "n_clicks"),
              Input("square-5", "n_clicks"),
              Input("square-6", "n_clicks"),
              Input("square-7", "n_clicks"),
              Input("square-8", "n_clicks"),
              Input("square-9", "n_clicks"))
def update_square_contents(*clicks):
    return [f"Square {n+1} Clicked {click} times" for n, click in enumerate(clicks)]

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
