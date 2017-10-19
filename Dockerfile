FROM ubuntu:14.04

# ENV variable
ENV INSTALL /opt/app
ENV NOTEBOOKS $INSTALL/notebooks
ENV FRAMEWORK $INSTALL/OpenWPM
# Jupyter Config File
ENV JUPYTER_CONFIG_DIR $INSTALL/ServeWPM
# Display
ENV DISPLAY :99
RUN export DISPLAY

# Dependencies
RUN apt-get update -y
RUN apt-get install -y git gunicorn sqlite3 libsqlite3-dev vim
RUN apt-get install -y xfonts-scalable xfonts-100dpi xfonts-75dpi xfonts-cyrillic

# Install OpenWPM
RUN git clone https://github.com/citp/OpenWPM $INSTALL/OpenWPM
WORKDIR $INSTALL/OpenWPM
RUN echo Y | sudo ./install.sh

# Install ServeWPM
ADD ServeWPM $INSTALL/ServeWPM
WORKDIR $INSTALL/ServeWPM
RUN pip install -U -r requirements.txt

# Install Notebooks
ADD notebooks $NOTEBOOKS

# Djanga Migrations
# RUN echo yes | python $INSTALL/ServeWPM/manage.py collectstatic
RUN python $INSTALL/ServeWPM/manage.py makemigrations
RUN python $INSTALL/ServeWPM/manage.py migrate
RUN echo "from django.contrib.auth.models import User; User.objects.filter(email='admin@example.com').delete(); User.objects.create_superuser('admin', 'admin@example.com', 'password')" | python manage.py shell

# Run
CMD Xvfb :99 -screen 0 1024x768x16 2>/dev/null >/dev/null & \
    cd $NOTEBOOKS && \
    python $INSTALL/ServeWPM/manage.py shell_plus --notebook & \
    cd $INSTALL/ServeWPM && \
    gunicorn ServeWPM.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3

# Http port
EXPOSE 8000
EXPOSE 8888

