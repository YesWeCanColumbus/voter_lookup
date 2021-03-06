import os, glob

path = os.path.join(os.path.dirname(__file__), 'data')
dbpath = os.path.join(path, 'voters-xapian')
datapaths = glob.glob(os.path.join(path, 'SWVF*.csv'))

fields = {'RESIDENTIAL_ZIP': 'Z',
          'COUNTY_NUMBER': 'C',
          'LAST_NAME': 'S',
          'FIRST_NAME': 'G',
          'MIDDLE_NAME': 'M',
          'PRECINCT_NAME': 'P',
          'RESIDENTIAL_ADDRESS1': 'RA',
          }

