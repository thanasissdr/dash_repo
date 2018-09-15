import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

import pandas as pd
import numpy as np
import requests

# ===========
# APPLICATION
# ===========

app = dash.Dash()

colors = {
    "background": "#111111",
    "text": "#7FDBFF"
}

app.layout = html.Div(
    style={"backgroundColor": colors["background"], "textAlign": "center"},
    children=[

        html.H1("Hello Dash", style={"color": colors["text"]}),

        html.Div("Dash: A web based application for Python", style={"color":
                                                                        colors[
                                                                            "text"]}),


        dcc.Graph(id="graph-object",
                  figure={
                      "data":[
                          {"x": [1, 2, 3, 4], "y":[4, 2, 3, 1], "type": "bar",
                              "name":
                              "San "
                                                                        "Francisco"},
                          {"x": [1, 2, 3, 4], "y": [5, 4, 3, 1], "type": "bar",
                              "name":
                              "Montreal"}
                      ],

                      "layout":{
                          "plot_bgcolor": colors["background"],
                          "paper_bgcolor": colors["background"],
                          "color": colors["text"]
                      }
                  })
    ])

if __name__ == "__main__":
    app.run_server()
