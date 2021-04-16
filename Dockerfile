FROM nginx:stable

RUN apt-get update --fix-missing
RUN apt-get install -y python3.7
RUN apt-get install -y python3-pip
RUN ln -s /usr/bin/python3 /usr/bin/python \
        && ln -s /usr/bin/pip3 /usr/bin/pip

WORKDIR /app

COPY requirement.txt /app
COPY ./infra_conf/default.conf /etc/nginx/conf.d

RUN pip install --upgrade pip \
        && pip install -r requirement.txt
