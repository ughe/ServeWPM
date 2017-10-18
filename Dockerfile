FROM ubuntu:14.04

# ENV variables
ENV INSTALL /opt/OpenWPM/
ENV DEBIAN_FRONTEND noninteractive 
ENV DISPLAY :99
RUN export DISPLAY

# Download OpenWPM
RUN apt-get update -y
RUN apt-get install -y git
RUN git clone https://github.com/citp/OpenWPM $INSTALL

# Install OpenWPM
WORKDIR $INSTALL
RUN echo Y | sudo ./install.sh

# Missing Xvfb
RUN apt-get install -y xfonts-scalable xfonts-100dpi xfonts-75dpi xfonts-cyrillic

# Run Script
CMD Xvfb :99 -screen 0 1024x768x16 2>/dev/null >/dev/null & \
    sleep 0.1 && python /opt/OpenWPM/demo.py

