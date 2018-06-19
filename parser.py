#!/usr/bin/env python3

import pandas as pd

def parse_attr(row):
    """
    Parse attributes row.

    Parameters
    ----------
    row : str
        Attribute value
    
    >>> row = "Cup:F|Band:28|Color:BLACK"
    {'Cup': 'F', 'Band': 28, 'Color': 'BLACK'}

    """
    parsed = {}
    
    for string in row.split("|"):
        parsed[string.split(':')[0]] = string.split(':')[1]  

    return parsed

def parse_df(df, col, id):
    """
    Format pd.DataFrame with parsed attributes in 
    separate columns.

    Parameters
    ----------
    df : pd.DataFrame
        Raw data with attributes col
    col : str
        Attributes col name
    id : str
        Unique ID in df
    
    Returns
    ----------
    pd.DataFrame

    """
    attrs = []

    for index, row in df.iterrows():
        if pd.notna(row[col]):
            row_attrs = parse_attr(row[col])
            row_attrs[id] = row[id]
            attrs.append(row_attrs)
           
    return pd.merge(df, pd.DataFrame(attrs), how='left', on=id)

