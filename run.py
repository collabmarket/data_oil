import yaml
import pandas as pd
import Quandl

try:
    get_ipython().magic(u'matplotlib inline')
except NameError:
    print "IPython console not available."

with open('data.yml') as fp:
  meta = yaml.load(fp)

for d in meta['eia']['monthly']:
    df = Quandl.get(d['code'])
    df.plot(title=d['varname'])
    df.to_csv(d['filename'])

for d in meta['eia']['weekly']:
    df = Quandl.get(d['code'])
    df.plot(title=d['varname'])
    df.to_csv(d['filename'])

for d in meta['eia']['annually']:
    df = Quandl.get(d['code'])
    df.plot(title=d['varname'])
    df.to_csv(d['filename'])
