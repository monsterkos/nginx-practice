FROM python:3.10-buster

ENV PROJECT_DIR /src/nginx-practice

RUN apt-get update && apt-get upgrade -y \
    && apt install -y sudo nginx \
    && rm -rf /var/lib/apt/lists/* \
    && pip3 install pipenv

RUN mkdir -p ${PROJECT_DIR}

WORKDIR ${PROJECT_DIR}
COPY . .

RUN  rm -rf /etc/nginx/nginx.conf \
     && rm -rf /etc/nginx/sites-enabled/* \
     && mv  ${PROJECT_DIR}/docker/nginx.conf /etc/nginx/nginx.conf \
     && mv  ${PROJECT_DIR}/docker/nginx.conf /etc/nginx/sites-enabled/

RUN pipenv install --system --deploy

EXPOSE 8080

CMD ["gunicorn", "-c", "nginx_practice/gunicorn.conf.py"]
