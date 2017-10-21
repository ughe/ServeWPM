# ServeWPM
ServeWPM is a docker image for running [OpenWPM](https://github.com/citp/OpenWPM).

ServeWPM can run OpenWPM locally with machines that have [Docker installed](https://www.docker.com/community-edition#/download). It can also be run remotely on AWS.

## Compontents
There are three main components: the [OpenWPM](https://github.com/citp/OpenWPM) framework, the Jupyter Notebook server used to run the tests, and the Django ORM (Object-Relational Mapping) layer for working with OpenWPM's output.

# Building the image
This step can take more than 10 minutes without any caching.
```bash
git clone https://github.com/ughe/ServeWPM && cd ServeWPM
docker build -t servewpm .
```

# Running the docker container
This deploys the Jupyter notebook to Port 80. Also opens port 8000.
```bash
docker run -p 80:8888 -p 8000:8000 servewpm
```

# Tutorial
Go to the URL (i.e. [127.0.0.1](127.0.0.1/)), and open the `README.ipynb` Jupyter notebook. The notebook starts by running a version of the `demo.py` example program from OpenWPM. Once the website tests are run, the tutorial continues with examining the output files in a directory called `$PROJECT_NAME/`.

N.B.: The password is `phosphoric3:historiographically` and the hash is set in the `ServeWPM/jupyter_notebook_config.py` file.

# Structure
The docker image creates three primary sibling directories: `OpenWPM`, the OpenWPM files; `ServeWPM`, the Django server with Jupyter integration; and `notebooks`, where all of the files are kept. 

In `notebooks`, there is a special directory called `exports` where Django looks for the `crawl-data.sqlite` file.

In order to import the `OpenWPM` project files from a Jupyter notebook in `notebooks`, the path is inserted before any OpenWPM imports:
```python
sys.path.insert(0, os.environ['FRAMEWORK'])
# OpenWPM imports below:
from automation import TaskManager, CommandSequence
```

# Django Server
The Django server is really great; although, it is not the focus of this image because it is peripheral to the data analysis, and AWS Elasticbeanstalk does not support single Docker containers exporting multiple ports.

First, create a new IPython notebook in Jupyter by using the `Django Shell-Plus` option.

Next, create a superuser (admin):
```python
from django.contrib.auth.models import User
User.objects.create_superuser('admin', 'admin@example.com', 'synthetics1126599/commencements')
```
Run this command next in the notebook to start the server:
```
!gunicorn ServeWPM.wsgi:application --bind 0.0.0.0:8000 --workers 3
```
Finally, go to admin on the 8000 port (i.e. [127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)) and log in.

For reference, the models were generated with `python $JUPYTER_CONFIG_DIR/manage.py inspectdb > $JUPYTER_CONFIG_DIR/export/models.py`. The output file `models.py` needs to be edited to conform to Django's rules about `id`'s.

# Deploying to AWS

## Warning:
ServeWPM is fine for local development. It is not advised to deploy online without caution. Security concerns include Jupyter Notebook's root access, preset passwords, [secret key](https://docs.djangoproject.com/en/1.11/ref/settings/#std:setting-SECRET_KEY), and more. 

## Process
First, compress four items together: the `Dockerfile`, `notebooks`, `ServeWPM` and `.ebextensions`.

For example, in unix you might use: `zip -r -X ServeWPM.zip .ebextensions Dockerfile notebooks ServeWPM`. On Windows, too, make sure to zip each individual item together, do not compress the parent directory.

In the AWS console, go to [ElasticBeanstalk](https://console.aws.amazon.com/elasticbeanstalk). Create a new environment in a new application. For the `Platform` choose `Preconfigured platform` then `Docker`. For `Application Code` choose `Upload your code` and upload the compressed project. Finally, choose `Create environment`. The deploy should take at least ten minutes as it builds the image instead of using an uploaded one.

