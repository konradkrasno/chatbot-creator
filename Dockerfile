FROM python:3.8
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip3 install -r requirements.txt
COPY . .
RUN chmod 666 ./boot.sh
EXPOSE 8000
