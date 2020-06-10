FROM python:3.8.3-slim

RUN apt-get update && apt-get install make

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "make", "run" ]