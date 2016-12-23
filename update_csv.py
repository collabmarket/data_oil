import os
import yaml
import time
import pandas as pd
import Quandl

with open('data.yml') as fp:
    meta = yaml.load(fp)

def file_exist(filename):
    return os.path.exists(filename)

def csv_is_update(d):
    csv_args = dict(index_col='Date', parse_dates=True)
    lq = Quandl.get(d['code'], row=0).tail(1).to_json()
    if file_exist(d['filename']):
        lf = pd.read_csv(d['filename'], **csv_args).tail(1).to_json()
    else:
        lf = 'Not exist'
    return lq == lf

def csv_update(d):
    df = Quandl.get(d['code'])
    df.to_csv(d['filename'])

for p in meta['eia'].keys():
    for d in meta['eia'][p]:
        if not csv_is_update(d):
            csv_update(d)
            time.sleep(5) # delays for 5 seconds
            print d['varname'],'(Updated)'

