FROM python:2

# ENV variable
ENV INSTALL /opt/app/ServeWPM
ENV NOTEBOOKS /opt/app/notebooks
# Jupyter Config File
ENV JUPYTER_CONFIG_DIR $INSTALL

# sqlite3 libsqlite3-dev apt-get

# Add & Install ServeWPM
ADD ServeWPM $INSTALL
WORKDIR $INSTALL
RUN pip install -U -r requirements.txt

# Djanga Migrations
RUN python $INSTALL/manage.py makemigrations
RUN python $INSTALL/manage.py migrate
RUN echo "from django.contrib.auth.models import User; User.objects.filter(email='admin@example.com').delete(); User.objects.create_superuser('admin', 'admin@example.com', 'password')" | python manage.py shell

# Jupyter
RUN mkdir $NOTEBOOKS || true

# Run
CMD cd $NOTEBOOKS && \
    python $INSTALL/manage.py shell_plus --notebook & \
    cd $INSTALL && \
    gunicorn ServeWPM.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3

# Http port
EXPOSE 8000
EXPOSE 8888

