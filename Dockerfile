FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN mkdir -p /home/app
WORKDIR /home/app
COPY ./ /home/app
RUN pip install -r requirements.txt
RUN python manage.py crontab add
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000