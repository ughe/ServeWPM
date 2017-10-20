# ServeWPM
ServeWPM is a docker image for running [OpenWPM](https://github.com/citp/OpenWPM).

## Warning:
ServeWPM is fine for local linux development. It is not advised to deploy online without caution. Security concerns include Jupyter Notebook's root access, preset passwords, and certificates. 

## Compontents
There are three main components: the [OpenWPM framework](https://github.com/citp/OpenWPM), the IPython Jupyter Notebook, and the Django ORM layer.

# Downloading the image
This may be significantly faster (instead of building the image).
```bash
git clone https://github.com/ughe/ServeWPM/releases/tag/v0.1.0/servewpm.tar
docker load servewpm.tar
```

# Building the image
This step can take 10 minutes without any caching.
```bash
git clone https://github.com/ughe/ServeWPM && cd ServeWPM
docker build -t servewpm .
```

# Running the docker container
This deploys the Jupyter notebook to Port 80. Also opens port 8000.
```bash
docker run -p 80:8888 -p 8000:8000 servewpm
```

## Jupyter
Once the docker container is running, go to [jupyter localhost](127.0.0.1/tree). You will be prompted to enter the password (may be: `phosphoric3:historiographically`). This is defined as a hash in the `ServeWPM/jupyter_notebook_config.py` file.

## Tutorial
Open the `README.ipynb` Jupyter notebook. The first code cell is a version of the `demo.py` example from OpenWPM with a modified import function and output dir. Execute the python or bash in cells with shift-enter. A `!` staring a cell means bash is being executed.

### Querying DB
The results database is stored in `PROJECT_NAME/crawl-data.sqlite`. The `PROJECT_NAME` is the first python and environmental variable set in `README.ipynb`. The database can either be queried directly through `sqlite3` or it can be attempted through django.

#### Querying DB: with Django
First, the output file is copied to the local `export` dir.
```bash
!cp $PROJECT_NAME/crawl-data.sqlite export/crawl-data.sqlite
```
Next the modules can be imported:
```python
from export.models import (
    Crawl,
    Crawlhistory,
    FlashCookies,
    HttpRequests,
    HttpResponses,
    Localstorage,
    ProfileCookies,
    SiteVisits,
    Task,
    Xpath,
)
```
Finally, the `__dict__` attribute can be used to explore more, or read `ServeWPM/export/models.py`. I.e.:
```python
svs = SiteVisits.objects.all()
s = svs[0]
s.__dict__
```

#### Querying DB: with Sqlite3
First, connect to the db:
```python
import sqlite3
rel_path = 'PROJECT_PATH/crawl-data.sqlite'
db = sqlite3.connect(rel_path)
cursor = db.cursor()
```
Then:
```python
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = list(zip(*cursor.fetchall())[0])
print(tables)
```
Then:
```python
pairs = []
for t in tables:
    cursor.execute("SELECT * from {}".format(t))
    elements = cursor.fetchall()
    pairs.append((t, elements))
```
Then:
```python
pairs[1]
```

### Import Explanation
The Jupyter notebooks are not in the same directory as OpenWPM, therefore the path needs to be added before any OpenWPM apps are imported.
Here is the OpenWPM path:
```python
import sys
import os
sys.path.insert(0, os.environ['FRAMEWORK'])
```
Here is the OpenWPM import:
```python
from automation import TaskManager, CommandSequence
```

### Example `openwpm.log` output:
```
TaskManager          - INFO     - 
...
========== Output (archive) profile dirs ==========
  No profile archive directories specified


BrowserManager       - INFO     - BROWSER 3: EXECUTING COMMAND: ('GET', 'http://www.example.com', 0, 3)
BrowserManager       - INFO     - BROWSER 2: EXECUTING COMMAND: ('GET', 'http://www.example.com', 0, 2)
...
BrowserManager       - INFO     - BROWSER 3: EXECUTING COMMAND: ('DUMP_PROFILE_COOKIES', 1508454416.26996, 8)
BrowserManager       - INFO     - BROWSER 1: EXECUTING COMMAND: ('DUMP_PROFILE_COOKIES', 1508454416.269908, 7)
CPU times: user 180 ms, sys: 100 ms, total: 280 ms
Wall time: 39 s
```

## Django Server
First, create a new IPython notebook in Jupyter, [127.0.0.1/tree](127.0.0.1/tree), by selecting `New` and then `Django Shell-Plus`.
Next, create a superuser:
```python
from django.contrib.auth.models import User
User.objects.create_superuser('admin', 'admin@example.com', 'synthetics1126599/commencements')
```
The Django server is not started by default because AWS only supports exposing one port (the first one in the Docker file). The server can still be started locally by running this in an IPython notebook:
```python
!gunicorn ServeWPM.wsgi:application --bind 0.0.0.0:8000 --workers 3
```
Next, login here: [127.0.0.1:8000/admin](127.0.0.1:8000/admin) as the superuser.

# Troubleshooting

## `WebDriverException: Message: connection refused`
Try running the webdriver directly to get the direct error:
```python
from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://www.princeton.edu')
browser.quit()
```
