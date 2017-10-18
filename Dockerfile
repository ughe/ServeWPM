FROM ubuntu:14.04

# ENV variables
ENV INSTALL /opt/app
ENV INSTALL_OPEN /opt/app/OpenWPM/
ENV INSTALL_SERVE /opt/app/ServeWPM/
ENV DISPLAY :99
RUN export DISPLAY

# Add & Install OpenWPM
RUN apt-get update -y
RUN apt-get install -y git
RUN git clone https://github.com/citp/OpenWPM $INSTALL/OpenWPM/
WORKDIR $INSTALL/OpenWPM/
RUN echo Y | sudo ./install.sh
# Missing Xvfb fonts
RUN apt-get install -y xfonts-scalable xfonts-100dpi xfonts-75dpi xfonts-cyrillic

# Add & Install ServeWPM
RUN apt-get install -y python-pip
ADD ServeWPM $INSTALL/ServeWPM/
WORKDIR $INSTALL/ServeWPM/
RUN sudo pip install -U -r requirements.txt

# Run Script
CMD Xvfb :99 -screen 0 1024x768x16 2>/dev/null >/dev/null & \
    gunicorn ServeWPM.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3

# Web server port
EXPOSE 8000

