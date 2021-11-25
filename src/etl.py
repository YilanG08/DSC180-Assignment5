import os
import pandas as pd

def get_data(outdir):
    '''
    Load data from test
    '''
    fp = os.path.join(outdir['outdir'])
    return pd.ExcelFile(fp,engine="openpyxl")

def get_sheet(data,sheet):
    return pd.read_excel(data, sheet)