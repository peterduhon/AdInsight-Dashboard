import pandas as pd

def get_ad_performance(conn, start_date, end_date):
    query = '''
    SELECT * FROM ad_performance
    WHERE date BETWEEN ? AND ?
    '''
    df = pd.read_sql_query(query, conn, params=(start_date, end_date))
    return df
