#!/usr/bin/env python3

import click
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from helpers import *

def clean_row(row, markup_type='lxml'):
    """
    Clean and format HTML-encoded description
    strings for Magento pages.

    >>> clean_row("<p>Product</p>&#013;&#013;&#010;<ul>'<li>Description</li>")
    "Product<br/>'Description"

    """
    output = ''

    if pd.notnull(row):
        output = BeautifulSoup(row, markup_type).get_text()

        # replace ASCII returns with HMTL breaks
        if '\n' or '\r' in output:
            output = replace_pattern(output, '[\r\n]', '<br/>')

    return output if output else np.nan 

def format_df(df, col):
    """
    Format pd.DataFrame HTML-encoded column.

    Parameters
    ----------
    df : pd.DataFrame
        Raw data
    col : str
        Col name
    
    Returns
    ----------
    pd.DataFrame

    """
    df[col] = df[col].apply(clean_row)

    return df


@click.command()
@click.argument('file_path')
@click.argument('col')
@click.option(
    '-e', '--export_path', 
    help='File export path.'
)
def main(file_path, col, export_path):
    """Format items.csv file with parsed attributes."""
    df = pd.read_csv(file_path)
    output = format_df(df, col)

    if export_path:
        output.to_csv(export_path, index=False)
    else:
        output.to_csv(file_path, index=False)


if __name__ == "__main__":
    main()
