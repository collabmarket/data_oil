import os
import yaml
import time
import pandas as pd
import Quandl

with open('data.yml') as fp:
    meta = yaml.load(fp)

def file_exist(filename):
    return os.path.exists(filename)

def csv_is_update(serie):
    csv_kargs = dict(index_col='Date', parse_dates=True)
    #~ Bugs from Quandl.get (row=0 give all data) (row=1 some cases give empty df)
    lq = Quandl.get(serie['code'], row=1).to_json()
    if file_exist(serie['filename']):
        lf = pd.read_csv(serie['filename'], **csv_kargs).iloc[[-2]].to_json()
    else:
        lf = 'Not exist'
    return lq == lf

def csv_update(serie):
    df = Quandl.get(serie['code'])
    df.to_csv(serie['filename'])

if __name__ == '__main__':
    print 'Start check for updates!'
    for period in meta['eia'].keys():
        for serie in meta['eia'][period]:
            if not csv_is_update(serie):
                csv_update(serie)
                # Delays for 5 seconds, prevent blocking from Quandl
                time.sleep(5)
                print serie['varname'],'(Updated)'
        print 'Check %s done.' % period
    print 'Finished!'
