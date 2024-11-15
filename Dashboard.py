from flask import Flask, render_template
import dash
import dash_core_components as dcc
import dash_html_components as html

app = Flask(__name__)

# Initialize Dash app within Flask
dash_app = dash.Dash(__name__, server=app, routes_pathname_prefix='/dashboard/')

dash_app.layout = html.Div([
    html.H1("Ball Mill Digital Twin Dashboard"),
    dcc.Graph(id='load-shape-graph'),
    dcc.Graph(id='power-draw-graph')
])

@app.route('/')
def home():
    return "Welcome to the Ball Mill Digital Twin Dashboard!"

# Run Flask app
if __name__ == '__main__':
    app.run(debug=True)
