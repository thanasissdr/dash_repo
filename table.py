import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

import pandas as pd

df = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/'
    'c78bf172206ce24f77d6363a2d754b59/raw/'
    'c353e8ef842413cae56ae3920b8fd78468aa4cb2/'
    'usa-agricultural-exports-2011.csv')

b = df.loc[0, :].values

app = dash.Dash()


def generate_table(df, max_rows=10):
    return html.Table(
        [html.Tr([html.Th(col) for col in df.columns])] +

        [html.Tr(
            [html.Td(i) for i in df.loc[k, :]]  # We turn each value
            # of each row of the dataframe into an html.Td element
        ) for k in range(0, max_rows)]
    )


app.layout = html.Div(style={"backgroundColor": "#111111", "color":
    "#7FBFDD", "textAlign": "center "},
                      children=[
                          html.H1(children="Creating a Dataframe table"),

                          html.Div(style={
                              "textAlign": "center"},children=generate_table(
                              df))
                      ]
                      )

if __name__ == "__main__":
    app.run_server()
