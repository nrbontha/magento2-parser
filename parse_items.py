#!/usr/bin/env python3

import pandas as pd

def parse_row(row):

    parsed = {}
    
    for string in row.split("|"):
        parsed[string.split(':')[0]] = string.split(':')[1]  

    return parsed

def parse_df(df, col, id):
    
    attrs = []

    for index, row in df.iterrows():
        if pd.notna(row[col]):
            row_attrs = parse_row(row[col])
            row_attrs[id] = row[id]
            attrs.append(row_attrs)
           
    return pd.merge(df, pd.DataFrame(attrs), how='left', on=id)

if __name__ == "__main__":

    df = pd.read_csv('data/items_raw.csv')
    clean = df[['ITEM_SID', 'STYLE_SID', 'SET', 'ATTR']] 

    export = parse_df(df, 'ATTR', 'ITEM_SID')
    export.to_csv('data/export.csv', index=False)

    export_clean = parse_df(clean, 'ATTR', 'ITEM_SID')
    export_clean.to_csv('data/export_clean.csv', index=False)
