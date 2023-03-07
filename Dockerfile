FROM python:3.9

WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y apt-transport-https
RUN echo 'deb http://private-repo-1.hortonworks.com/HDP/ubuntu14/2.x/updates/2.4.2.0 HDP main' >> /etc/apt/sources.list.d/HDP.list
RUN echo 'deb http://private-repo-1.hortonworks.com/HDP-UTILS-1.1.0.20/repos/ubuntu14 HDP-UTILS main'  >> /etc/apt/sources.list.d/HDP.list
RUN echo 'deb [arch=amd64] https://apt-mo.trafficmanager.net/repos/azurecore/ trusty main' >> /etc/apt/sources.list.d/azure-public-trusty.list
RUN apk add --update linux-headers
RUN apt-get  update
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt --upgrade pip
COPY . .