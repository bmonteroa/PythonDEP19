import pandas as pd

def extract_table(tabla,conn):
    df = pd.read_sql(f"select * from {tabla}", con= conn)
    return df