# this will be moved to it's own repo

FROM ubuntu:xenial
RUN apt-get update
RUN apt-get install  -y ssh python3-pip libffi-dev libssl-dev
#RUN pip3 install -r requirements.txt
#RUN pip3 install --upgrade pip
COPY . /app
WORKDIR /app
ENV ENV_PASSWORD=testytest
CMD /bin/bash /app/setup.sh


