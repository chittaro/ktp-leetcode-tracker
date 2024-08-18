from dash import Dash
import pandas as pd


df = pd.DataFrame()
print(df)

app = Dash(__name__, external_stylesheets=['style.css'])
