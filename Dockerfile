FROM python:3.10.4-slim-buster
RUN apt-get update --fix-missing && apt-get upgrade -y
RUN apt-get install -y git wget python3-pip curl bash neofetch ffmpeg software-properties-common
COPY requirements.txt .

RUN pip3 install wheel
RUN pip3 install --no-cache-dir -U -r requirements.txt
WORKDIR /app
COPY . .

CMD flask run -h 0.0.0.0 -p 8000 & python3 -m crushe
# CMD gunicorn app:app & python3 -m crushe
