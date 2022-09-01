# from python 3 ubuntu image

FROM ubuntu:latest
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN apt update && apt upgrade -y

RUN apt install -y python3-pip

RUN mkdir -p /home/app
RUN apt-get install -y cron
WORKDIR /home/app
COPY ./ /home/app
RUN service cron start
RUN apt-get install -y systemctl
RUN systemctl enable cron
RUN systemctl start cron
RUN pip install -r requirements.txt
RUN python3 manage.py crontab add
RUN chmod +x ./startup.sh
CMD ["./startup.sh"]

EXPOSE 8000