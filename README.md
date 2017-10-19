# ServeWPM
ServeWPM is a docker image that runs OpenWPM.

## Warning:
Do not push this image to any aws instance as the jupyter configuration has major security vulnerabilities. It is possible to just package up the OpenWPM part in a docker container, which would be more safe.

## Compontents
There are three main components: the [OpenWPM framework](https://github.com/citp/OpenWPM), the Django ORM layer, and the IPython Jupyter Notebook.

# Building the image
This step may take as long as ten minutes.
```bash
git clone https://github.com/ughe/ServeWPM && cd ServeWPM
docker build -t servewpm .
```

# Downloading the image
This may be significantly faster
```bash
git clone https://github.com/ughe/ServeWPM/releases/1/servewpm.tar
docker load servewpm.tar
```

# Running the docker container
```bash
docker run -p 8000:8000 -p 8888:8888 servewpm
```

## What I get locally:
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

# Tutorial
Once you have the docker container running, go to [127.0.0.1:8888](127.0.0.1:8888) and log into the Jupyter notebook interface. From there, open the `README.ipynb` and run the `demo.py` program.
