FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /web_scraping/
WORKDIR /web_scraping/
ADD requirements.txt /web_scraping/
RUN pip install -r requirements.txt
ADD . /web_scraping/
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]