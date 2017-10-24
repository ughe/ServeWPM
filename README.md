# ServeWPM
ServeWPM is a docker image for running [OpenWPM](https://github.com/citp/OpenWPM).

ServeWPM can run OpenWPM locally with machines that have [Docker installed](https://www.docker.com/community-edition#/download). It can also be run remotely on AWS.

## Compontents
There are three main components: the OpenWPM framework, the Jupyter Notebook server used to run the tests, and the Django ORM (Object-Relational Mapping) layer for working with OpenWPM's output.

# Getting Started 

## Building the image
This step can take more than 10 minutes without any caching.

The `passwd()` function will prompt for a **new password** that is used to protect the Jupyter Notebook.
```bash
git clone https://github.com/ughe/ServeWPM ServeWPM
cd ServeWPM
docker build \
    --build-arg DJANGO_SECRET_KEY=$(python -c 'from django.core.management.utils import get_random_secret_key; print get_random_secret_key()') \
    --build-arg HOST_IP=0.0.0.0 \
    --build-arg JUPYTER_PASSWORD_HASH=$(python -c 'from notebook.auth import passwd; print passwd()') \
    -t servewpm .
```

## Running the docker container
This deploys the Jupyter notebook to Port 80. Also opens port 8000 for the optional Django server. The `-d` flag can be added to run the docker container in the background.
```bash
docker run -p 80:80 -p 8000:8000 servewpm
```

## Tutorial
Go to the URL (i.e. [127.0.0.1](127.0.0.1/)), and open the `README.ipynb` Jupyter notebook. The notebook starts by running a version of the `demo.py` example program from OpenWPM. Once the website tests are run, the tutorial continues with examining the output files in a directory called `$PROJECT_NAME/` using the Django ORM and Sqlite3.

N.B.: The password is the value set when the image was built.

## More Docker Commands

### SSH into Container
```bash
docker exec -it $(docker ps -q) bash
```
This works if there is only one container running. Otherwise, first run `docker ps` and then `docker exec -it ef2e47fbfa1b bash` where `ef2e47fbfa1b` is the `CONTAINER ID` of the correct container instance.

### Saving and loading an image
This will expose the secret key or password hash if public.
```bash
docker save servewpm -o servewpm.tar
docker load -i servewpm.tar
```

### Halting ALL docker containers
```bash
docker kill $(docker ps -q)
```

# Project Structure
The docker image creates three primary sibling directories: `OpenWPM`, `ServeWPM` (django), and `notebooks`. 

In `notebooks`, there is a special directory called `exports` where Django looks for the `crawl-data.sqlite` file.

In order to import the `OpenWPM` project files from a Jupyter notebook in `notebooks`, the path is inserted before any OpenWPM imports:
```python
sys.path.insert(0, os.environ['FRAMEWORK'])
# OpenWPM imports below:
from automation import TaskManager, CommandSequence
```

# Django Server
The Django Server provides a framework for interacting with the ORM and serving web pages.

To log into the admin site, the credentials need to be set up. First, create a new IPython notebook in Jupyter by using the `Django Shell-Plus` option.

Next, create a superuser (admin):
```python
from django.contrib.auth.models import User
User.objects.create_superuser('admin', 'admin@example.com', 'CHANGE_ME')
```
Finally, go to admin on the 8000 port (i.e. [127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)) and log in.

For reference, the Django `export` models were generated with `python $DJANGO/manage.py inspectdb > $DJANGO/export/models.py`. The output file `models.py` needs to be edited to conform to Django's rules about `id`'s.

# Deploying to AWS

## Warning:
ServeWPM is fine for local development. It is not advised to deploy online without caution. Security concerns include Jupyter Notebook's root access, password handling, and more. 

## EC2
Manually deploying to an EC2 instance is one option. 

After configuring a new instance, including its Security Group, and launching it, create a key pair. Then select the instance on the dashboard and choose `Connect`. Replace `EC2`, below, with the dns (i.e. ec2-xx-xxx-xxx-xx.compute-1.amazonaws.com) of the instance. Also replace `CERT` with the path to the certificate. `servewpm.tar` should be in the current working directory. Then run the script below.

```bash
CERT="certificate.pem"
# i.e. EC2=ec2-user@ec2-48-458-381-20.compute-1.amazonaws.com
EC2=
scp -i $CERT servewpm.tar $EC2:/home/ec2-user
ssh -i $CERT $EC2 sudo yum update -y
ssh -i $CERT $EC2 sudo yum install -y docker
ssh -i $CERT $EC2 sudo service docker start
ssh -i $CERT $EC2 sudo docker load -i /home/ec2-user/servewpm.tar
ssh -i $CERT $EC2 sudo docker run -d -p 80:80 -p 8000:8000 servewpm
```

## Elastic Beanstalk
ElasticBeanstalk does not fully support Docker because there is no option for setup Args and the `OpenWPM` build actually fails when deployed by EB with a `WebDriverException: Message: connection refused`. This issue does not occur in the docker container locally on Mac, Windows 10, or a manually-configure Amazon or Ubuntu EC2 instance.

To attempt an EB deployment, compress the ServeWPM files. In unix you might use: `zip -r -X ServeWPM.zip .ebextensions Dockerfile notebooks ServeWPM`. On Windows, too, make sure to zip each individual item together, do not compress the parent directory.

In the AWS console, go to [ElasticBeanstalk](https://console.aws.amazon.com/elasticbeanstalk). Create a new environment in a new application. For the `Platform` choose `Preconfigured platform` then `Docker`. For `Application Code` choose `Upload your code` and upload the compressed project. Finally, choose `Create environment`. The deploy may take at least fifteen minutes as it builds the image instead of using a pre-built one.
