FROM ubuntu:14.04

# ARGS
ARG DJANGO_SECRET_KEY
ARG HOST_IP
ARG JUPYTER_PASSWORD_HASH
ENV DJANGO_SECRET_KEY ${DJANGO_SECRET_KEY}
ENV HOST_IP ${HOST_IP}
ENV JUPYTER_PASSWORD_HASH ${JUPYTER_PASSWORD_HASH}

# ENV variables
ENV INSTALL /opt/app
ENV NOTEBOOKS $INSTALL/notebooks
ENV FRAMEWORK $INSTALL/OpenWPM
ENV DJANGO $INSTALL/ServeWPM
ENV JUPYTER_CONFIG_DIR $DJANGO
ENV DISPLAY :99

# Dependencies
RUN apt-get update -y
RUN apt-get install -y git gunicorn sqlite3 vim
RUN apt-get install -y xfonts-scalable xfonts-100dpi xfonts-75dpi xfonts-cyrillic

# Install OpenWPM
RUN git clone https://github.com/citp/OpenWPM $FRAMEWORK
WORKDIR $FRAMEWORK
RUN echo Y | ./install.sh

# Install ServeWPM
ADD ServeWPM $DJANGO
WORKDIR $DJANGO
RUN pip install -U -r requirements.txt

# Install Notebooks
ADD notebooks $NOTEBOOKS
WORKDIR $NOTEBOOKS
RUN git init

# Django
RUN echo yes | python $DJANGO/manage.py collectstatic && \
    python $DJANGO/manage.py makemigrations && \
    python $DJANGO/manage.py migrate

# Run Django Server (optional) and 
CMD Xvfb $DISPLAY -screen 0 1366x768x16 2>/dev/null >/dev/null & \
    cd $NOTEBOOKS && \
    python $INSTALL/ServeWPM/manage.py shell_plus --notebook

# Export Jupyter Port 80. Django 8000.
EXPOSE 80 8000
