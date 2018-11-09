"""
    Get .csv files from given urls
"""

import zipfile, urllib, os, requests
from urllib.request import Request, urlopen, urlretrieve

# construct url
def urls(date):
    yyyy, mm, dd = date
    return "http://data.gdeltproject.org/events/{0:}{1:02d}{2:02d}.export.CSV.zip".format(yyyy, mm, dd)

# saves dates as list
dates = []

# 2013/04/01 - 2013/12/31
for j in range(3,12):
    for k in range(31):
        dates.append([2013, j+1, k+1])

# 2014/01/01 - 2017/12/31
for i in range(2014, 2017):
    for j in range(12):
        for k in range(31):
            dates.append([i, j+1, k+1])

# 2018/01/01 - 2018/10/31
for j in range(1,10):
    for k in range(31):
        dates.append([2018, j+1, k+1])

def get_files(dates):
    try:
        for date in dates:
            base_url = urls(date)  # construct urls for all dates
            request = requests.get(base_url)
            if request.status_code == 200:  # url exists # in order to ignore MissingException on missing urls
                local_filename, headers = urllib.request.urlretrieve(url = base_url)
                zip_ref = zipfile.ZipFile(file = local_filename, mode='r')  # original downloaded files are .zip
                zip_ref.extractall(path="C:/Users/rupal/Desktop/Gdelt_dump/")  # extract content in the given location
                zip_ref.close()
    except:
        pass


## main
if __name__ == '__main__':
    get_files(dates)
