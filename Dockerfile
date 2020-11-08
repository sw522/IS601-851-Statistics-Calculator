FROM python:3.7

ADD . .

RUN pip install --upgrade pip
RUN pip install numpy
RUN pip install scipy

CMD ["python", "-m", "unittest", "discover", "-s","Tests"]