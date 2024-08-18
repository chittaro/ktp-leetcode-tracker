from dash import Dash, html, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px



df = pd.DataFrame(
    [["11/2", 5, "Easy"],
     ["11/2", 2, "Medium"],
     ["11/2", 1, "Hard"],
     ["11/3", 6, "Easy"],
     ["11/3", 10, "Medium"],
     ["11/3", 3, "Hard"],
     ["11/4", 10, "Easy"],
     ["11/4", 15, "Medium"],
     ["11/4", 20, "Hard"],]
    , columns=["Date", "Count", "Difficulty"])
colors = ["#58db72", "#ebda60", "#e33636"]
fig = px.area(df, x="Date", y="Count", color="Difficulty", color_discrete_sequence=colors)


app = Dash(__name__, external_stylesheets=['style.css'])
server = app.server
app.title = f'KTP LeetCode Tracker'
app.layout = html.Div([
    html.H1("KTP LeetCode Tracker"),
    dcc.Graph(figure=fig, id='stacked-line-graph')
])



# @callback(
#     Output(component_id='stacked-line-graph', component_property='figure'),
# )
# def update_graph():
#     fig = px.area(df, x="Date", y="Count", color="Difficulty")
#     return fig

if __name__ == '__main__':
    app.run(debug=True)