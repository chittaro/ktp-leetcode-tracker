from dash import Dash, html, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import json


with open("bin/counts.json", "r") as file:
    jsonData = json.load(file)

df = pd.DataFrame.from_dict(jsonData["logs"])
colors = ["#58db72", "#ebda60", "#e33636"]
fig = px.area(df, x="date", y="count", color="difficulty", color_discrete_sequence=colors)


app = Dash(__name__, external_stylesheets=['static/style.css'])
server = app.server
app.title = f'KTP LeetCode Tracker'
app.layout = html.Div([
    html.H1("KTP LeetCode Tracker"),
    dcc.Graph(figure=fig, id='stacked-line-graph')
], className="main-div")



if __name__ == '__main__':
    app.run(debug=True)