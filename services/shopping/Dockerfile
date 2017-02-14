FROM python:3.6-alpine

RUN pip install -U pip
RUN mkdir /app

COPY requirements.txt /app
RUN pip install -r /app/requirements.txt
COPY his.almanac-0.0.1-py3-none-any.whl /app
RUN pip install /app/his.almanac-0.0.1-py3-none-any.whl

COPY src /app
CMD ["python", "-u", "/app/bootstrap.py"]
