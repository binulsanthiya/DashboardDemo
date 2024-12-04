import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# Load the dataset
crick_df = pd.read_csv('cricket_data (2).csv')

# Initialize Dash app
app = dash.Dash(__name__)

# Layout
app.layout = html.Div([
    html.H1("ICC Men's Cricket World Cup Dashboard", style={'textAlign': 'center'}),

    dcc.Dropdown(
        id='year-dropdown',
        options=[{'label': year, 'value': year} for year in sorted(crick_df['world_cup_year'].unique())],
        placeholder="Select World Cup Year",
    ),
    dcc.Graph(id='match-category-bar'),
    dcc.Graph(id='team-performance'),
])


# Callbacks for interactivity
@app.callback(
    Output('match-category-bar', 'figure'),
    [Input('year-dropdown', 'value')]
)
def update_category_chart(selected_year):
    if selected_year:
        filtered_df = crick_df[crick_df['world_cup_year'] == selected_year]
        fig = px.bar(filtered_df, x='match_category', title=f'Match Categories in {selected_year}')
        return fig
    return px.bar(crick_df, x='match_category', title='Match Categories')


@app.callback(
    Output('team-performance', 'figure'),
    [Input('year-dropdown', 'value')]
)
def update_team_chart(selected_year):
    if selected_year:
        filtered_df = crick_df[crick_df['world_cup_year'] == selected_year]
        fig = px.bar(filtered_df, x='team_1', y='team_1_runs', title=f'Team Performances in {selected_year}')
        return fig
    return px.bar(crick_df, x='team_1', y='team_1_runs', title='Team Performances')


if __name__ == '__main__':
    app.run_server(debug=True)
