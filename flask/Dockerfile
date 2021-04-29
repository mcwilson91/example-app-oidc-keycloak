FROM python:3.6.1-alpine
WORKDIR /project
ADD ./app /project/app
ADD ./app/client_secrets.json /project/instance/
RUN pip install -r app/requirements.txt
ENV FLASK_APP=app
EXPOSE 5000
CMD ["flask","run","--host","0.0.0.0"]
