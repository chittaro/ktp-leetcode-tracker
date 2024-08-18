from dash import Dash, html
import pandas as pd


df = pd.DataFrame({"Monday": {"Easy": 10, "Medium": 5, "Hard": 2}, "Tuesday": {"Easy": 14, "Medium": 6, "Hard": 2}})

app = Dash(__name__, external_stylesheets=['style.css'])
app.title('KTP LeetCode Tracker')

app.layout = [html.Div(children='Hello World')]

if __name__ == '__main__':
    app.run(debug=True)