FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /web_scraping_api/
WORKDIR /web_scraping_api/
ADD requirements.txt /web_scraping_api/
RUN pip install -r requirements.txt
ADD . /web_scraping_api/
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]