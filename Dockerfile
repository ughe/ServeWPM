FROM ubuntu:14.04

# ENV variables
ENV INSTALL /opt/app
ENV DISPLAY :99
RUN export DISPLAY

# Add & Install ServeWPM
ADD ServeWPM $INSTALL
WORKDIR $INSTALL/ServeWPM
RUN sudo pip install -U -r requirements.txt

# Add & Install OpenWPM
ADD https://github.com/citp/OpenWPM $INSTALL
WORKDIR $INSTALL/OpenWPM
RUN echo Y | sudo ./install.sh

# Missing Xvfb fonts
RUN apt-get install -y xfonts-scalable xfonts-100dpi xfonts-75dpi xfonts-cyrillic

# Run Script
WORKDIR $INSTALL/ServeWPM
CMD Xvfb :99 -screen 0 1024x768x16 2>/dev/null >/dev/null & \
    gunicorn ServeWPM.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3

# Web server port
EXPOSE 8000
