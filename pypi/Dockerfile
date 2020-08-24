FROM python:slim-buster as base

FROM base as prepare
ENV mirror='https://pypi.tuna.tsinghua.edu.cn/simple'
COPY ./requirements.txt .
RUN pip install -r /requirements.txt -i $mirror

FROM base
COPY --from=prepare /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages 
COPY . /app
WORKDIR /app

