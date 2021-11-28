FROM python:3

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

ADD https://raw.githubusercontent.com/mackliet/church_of_jesus_christ_api/master/church_of_jesus_christ_api/church_of_jesus_christ_api.py /opt/
COPY *.py /opt/

CMD /opt/run.py