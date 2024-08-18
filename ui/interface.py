from dash import Dash, html
import pandas as pd
import plotly.express as px


df = pd.DataFrame(
    [["11/2", 5, "Easy"], ["11/2", 2, "Medium"], ["11/3", 6, "Easy"], ["11/3", 10, "Medium"]]
, columns=["Date", "Count", "Difficulty"])
fig = px.area(df, x="Date", y="Count", color="Difficulty")

app = Dash(__name__, external_stylesheets=['style.css'])
server = app.server
app.title = f'KTP LeetCode Tracker'


app.layout = [html.Div(children='Hello World')]

if __name__ == '__main__':
     app.run(debug=True)