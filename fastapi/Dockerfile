FROM docker.io/nickgryg/alpine-pandas:latest
ADD requirements.txt /opt/dockerApp/requirments.txt
ADD run.py /opt/dockerApp/run.py
ADD app.ini /opt/dockerApp/app.ini
COPY app /opt/dockerApp/app
WORKDIR /opt/dockerApp
RUN pip install -r requirments.txt
EXPOSE 8080
CMD ["python", "/opt/dockerApp/run.py"]

#Build image with docker office image
#FROM python:3.9.10-alpine3.15
#RUN apk update && apk upgrade
#RUN apk add libpq-dev
#RUN apk add make automake gcc g++ subversion python3-dev
#RUN /usr/local/bin/python -m pip install --upgrade pip
#RUN pip install pandas -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
