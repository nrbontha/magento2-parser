#!/usr/bin/env python3

import pandas as pd

if __name__ == "__main__":

    df = pd.read_csv('data/items_raw.csv')
    clean = df[['ITEM_SID', 'STYLE_SID', 'SET', 'ATTR']] 

    export = parse_df(df, 'ATTR', 'ITEM_SID')
    export.to_csv('data/export.csv', index=False)

    export_clean = parse_df(clean, 'ATTR', 'ITEM_SID')
    export_clean.to_csv('data/export_clean.csv', index=False)
