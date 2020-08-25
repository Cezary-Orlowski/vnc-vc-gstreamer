FROM oott123/docker-novnc

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y curl wget nano ca-certificates software-properties-common && \
    apt-get install -y xfce4 xfce4-goodies && \
    apt-get install -y network-manager dbus-x11 xfonts-100dpi xfonts-75dpi xfonts-base xfonts-scalable

# Budgie Desktop
#RUN add-apt-repository ppa:budgie-remix/ppa
#RUN apt-get update
#RUN apt-get install -y budgie-desktop-environment

# ---------------------------------------------------------------

# nodejs
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - \
    && apt-get install -y nodejs

# chrome
RUN curl -sS https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | tee /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable
ENV CHROME_ARGS --no-sandbox

# VS Code
RUN curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg && \
    mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg && \
    sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list'
RUN apt-get update && apt-get install -y code # or code-insiders

# GStreamer
RUN apt-get install -y libgstreamer1.0-0 gstreamer1.0-plugins-base gstreamer1.0-plugins-good \
    gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-doc \
    gstreamer1.0-tools gstreamer1.0-x gstreamer1.0-alsa gstreamer1.0-pulseaudio
	
# Python
RUN curl https://bootstrap.pypa.io/get-pip.py --output get-pip.py \
	&& python get-pip.py \
	&& python2 get-pip.py \
	&& python3 get-pip.py \
	&& pip install pika mysql.connector \
	&& pip2 install pika mysql.connector \
	&& pip3 install pika mysql.connector



# Autoremove & Clean
RUN apt-get autoremove -y && \
    apt-get clean

# Set bash as default user terminal shell
RUN chsh -s /bin/bash user

# ---------------------------------------------------------------

COPY config/xstartup /etc/vnc/xstartup
RUN chmod u+x /etc/vnc/xstartup

EXPOSE 5911
