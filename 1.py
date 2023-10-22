import pandas as pd
import datetime
from datetime import datetime 
import os.path as path
if path. exists ('to do.csv'):
    to_do = pd.read_csv('to_do.csv', header=0)
else:
    columns = ['date due','item', 'priority']
    to_do = pd.DataFrame (columns=columns)
action = ' '