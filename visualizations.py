import plotly.express as px

def create_time_series_chart(df):
    fig = px.line(df, x='date', y='clicks', title='Clicks Over Time')
    return fig
