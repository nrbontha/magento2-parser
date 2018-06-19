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

