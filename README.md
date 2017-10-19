# ServeWPM
ServeWPM is a docker image for running [OpenWPM](https://github.com/citp/OpenWPM).

## Warning:
ServeWPM is fine for local linux development. It is not advised to deploy online without caution. Security concerns include Jupyter Notebook's root access, preset passwords, and certificates. 

## Compontents
There are three main components: the [OpenWPM framework](https://github.com/citp/OpenWPM), the IPython Jupyter Notebook, and the Django ORM layer.

# Building the image
This step can take 10 minutes without any caching.
```bash
git clone https://github.com/ughe/ServeWPM && cd ServeWPM
docker build -t servewpm .
```

# Running the docker container
This deploys the Jupyter notebook to Port 80 and the Django server to Port 8000.
```bash
docker run -p 80:8888 -p 8000:8000 servewpm
```

## Tutorial
Open [127.0.0.1/tree](127.0.0.1/tree) and then open the `README.ipynb` file. Press shift-enter to execute an IPython cell. Executing the first program in the notebook will run OpenWPM. After it is finished running (expect less than a minute), the next steps load the output file `crawl-data.sqlite` into the Django ORM folder.

## Logging In
Jupyter Notebook: [127.0.0.1/tree](127.0.0.1/tree)
Django Admin: [127.0.0.1:8000/admin](127.0.0.1:8000/admin)

Once the docker container is running, go to [jupyter localhost](127.0.0.1/tree). You will be prompted to enter the password `phosphoric3:historiographically`. This can be reset in the `ServeWPM/jupyter_notebook_config.py` file. To create a superuser for the [django side](127.0.0.1:8000/admin), create a new IPython notebook by clicking `New` and `Django Shell-Plus`. Next copy and paste this code, then press shift-enter to execute it:

```python
from django.contrib.auth.models import User
User.objects.create_superuser('admin', 'admin@example.com', 'synthetics1126599/commencements')
```

## Example bash output:
```bash
$ docker run -p 8000:8000 -p 8888:8888 servewpm
[2017-10-19 07:36:27 +0000] [7] [INFO] Starting gunicorn 19.7.1
[2017-10-19 07:36:27 +0000] [7] [INFO] Listening at: http://0.0.0.0:8000 (7)
[2017-10-19 07:36:27 +0000] [7] [INFO] Using worker: sync
[2017-10-19 07:36:27 +0000] [16] [INFO] Booting worker with pid: 16
[2017-10-19 07:36:27 +0000] [23] [INFO] Booting worker with pid: 23
[2017-10-19 07:36:27 +0000] [26] [INFO] Booting worker with pid: 26
[I 02:36:28.174 NotebookApp] Writing notebook server cookie secret to /root/.local/share/jupyter/runtime/notebook_cookie_secret
[I 02:36:28.196 NotebookApp] Serving notebooks from local directory: /opt/app/ServeWPM
[I 02:36:28.196 NotebookApp] 0 active kernels
[I 02:36:28.197 NotebookApp] The Jupyter Notebook is running at:
[I 02:36:28.197 NotebookApp] http://0.0.0.0:8888/
[I 02:36:28.197 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
```

# Downloading the image
This may be significantly faster (instead of building the image).
```bash
git clone https://github.com/ughe/ServeWPM/releases/tag/v0.1.0/servewpm.tar
docker load servewpm.tar
```
