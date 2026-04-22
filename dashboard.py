import dash
from dash import html, dcc, Input, Output
import plotly.express as px
import pandas as pd
from db import get_all_logs, get_logs_by_product
from generate_data import PRODUCTS

rows = get_all_logs()
# ! column names should be pulled from db, not hard coded
df = pd.DataFrame(rows, columns=['id', 'timestamp', 'product_name', 'quantity', 'assembler_id', 'utilization_rate', 'defect_count', 'lead_time'])

app = dash.Dash(__name__)
fig = px.bar(df, x='timestamp', y='utilization_rate', color='assembler_id', title='Utilization Rate Over Time')
app.layout = html.Div([
    html.H1("Factorio Manufacturing Dashboard"),
    dcc.Dropdown(
        id='product_dropdown',
        options=[{'label': p, 'value': p} for p in PRODUCTS],
        value=PRODUCTS[0]
    ),
    dcc.Graph(id='utilization_chart', figure=fig),
])

@app.callback(
    Output('utilization_chart', 'figure'),
    Input('product_dropdown', 'value')
)
def update_chart(selected_product):
    rows = get_logs_by_product(product_name=selected_product)
    # also hardcoded here lol
    filtered_df = pd.DataFrame(rows, columns=['id', 'timestamp', 'product_name', 'quantity', 'assembler_id', 'utilization_rate', 'defect_count', 'lead_time'])
    return px.bar(filtered_df, x='timestamp', y='utilization_rate', color='assembler_id', title='Utilization Rate Over Time')

if __name__ == "__main__":
    app.run(debug=True)