import sys
import os
import json
import pandas as pd

sys.path.insert(0, 'src')

import env_setup
from etl import get_data
from etl import get_sheet
from eda import find_cycle
from eda import clean_data
from eda import graph_CBT_LA


def main(targets):
    '''
    store the plot(EDA) of the data on the root
    '''
    if 'test' in targets:
        with open('config/data-params.json') as fh:
            data_cfg = json.load(fh)

        data = get_data(data_cfg) 
        rows, cols = get_sheet(data,'FemTemp').shape
        femtemp = get_sheet(data,'FemTemp')
        femact = get_sheet(data,'FemAct')
        maletemp = get_sheet(data,'MaleTemp')
        maleact = get_sheet(data,'MaleAct')
        total = [femtemp,femact,maletemp,maleact]

        graph_CBT_LA(total,rows)

    return 



if __name__ == '__main__':
    # run via:
    # python main.py data features model
    targets = sys.argv[1:]
    main(targets)