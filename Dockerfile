FROM python:3.10-buster

ENV PROJECT_DIR /src/nginx-practice

RUN apt-get update && apt-get upgrade -y \
    && apt install -y sudo nginx \
    && rm -rf /var/lib/apt/lists/* \
    && pip3 install pipenv

RUN mkdir -p ${PROJECT_DIR}

WORKDIR ${PROJECT_DIR}
COPY . .

# TODO : nginx conf 관련 설정 추가

RUN pipenv install --system --deploy

EXPOSE 80

CMD ["gunicorn", "-c", "nginx_practice/gunicorn.conf.py"]
