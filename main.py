import dash
from dash import dcc, html, dash_table
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import random

# Función para generar datos aleatorios para el reporte general
def generate_random_data():
    return {
        "Tiendas Activas": random.randint(50, 100),
        "Tiendas Cerradas": random.randint(10, 30),
        "Venta año pasado": round(random.uniform(5000000, 10000000), 2),
        "Venta últimos 12 meses": round(random.uniform(6000000, 12000000), 2),
        "Venta Proyectada anual": round(random.uniform(7000000, 14000000), 2),
        "Venta año actual": round(random.uniform(5500000, 11000000), 2)
    }

# Datos aleatorios para el resumen distrital
districts = ["District A", "District B", "District C"]
resumen_distrital_data = {
    "District": districts,
    "Sales": [round(random.uniform(1000000, 5000000), 2) for _ in range(len(districts))]
}

# Generar datos aleatorios para el gráfico de tiendas activas
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
active_stores_data = {
    "Month": months,
    "Active Stores": [random.randint(50, 100) for _ in range(len(months))]
}

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define layout
app.layout = dbc.Container([
    dbc.Row(html.H1("Reporte General del formato Mass"), className="Nombre_Reporte_General"),
    dbc.Row([
        html.Div(
            children=[
                html.Div(children=[
                    html.H2("# Tiendas Activas", className="label_texto"),
                    html.H2("# Tiendas Cerradas", className="label_texto"),
                    html.H2("Venta 2023", className="label_texto"),
                    html.H2("Venta ult 12 meses", className="label_texto"),
                    html.H2("Venta Proy. anual", className="label_texto"),
                    html.H2("Venta 2024", className="label_texto")
                ], style={"padding-left": "10px"}),
                html.Div(children=[
                    html.H1(generate_random_data()["Tiendas Activas"], className="label_valores_texto"),
                    html.H1(generate_random_data()["Tiendas Cerradas"], className="label_valores_texto"),
                    html.H1('$ ' + str(generate_random_data()["Venta año pasado"]), className="label_valores_texto"),
                    html.H1('$ ' + str(generate_random_data()["Venta últimos 12 meses"]), className="label_valores_texto"),
                    html.H1('$ ' + str(generate_random_data()["Venta Proyectada anual"]), className="label_valores_texto"),
                    html.H1('$ ' + str(generate_random_data()["Venta año actual"]), className="label_valores_texto")
                ], style={"padding-left": "10px"}),
            ])
    ], className="Cabecera_General"),
    html.Br(),
    dbc.Row([
        dash_table.DataTable(data=resumen_distrital_data, columns=[{"name": i, "id": i} for i in resumen_distrital_data.columns],
                             style_cell={'textAlign': 'center'},
                             style_header={'backgroundColor': 'blue', 'fontWeight': 'bold', 'color': 'white'}),
    ], className="Resumen_Distrital_Activas"),
    dbc.Row([
        dcc.Graph(figure=go.Figure(data=[go.Bar(x=active_stores_data["Month"], y=active_stores_data["Active Stores"])]))
    ], className="Grafico_Activas"),
], fluid=True)

if __name__ == "__main__":
    app.run_server(debug=True)
