from python:3

RUN pip install -r requirements.txt

COPY *.py /opt/
