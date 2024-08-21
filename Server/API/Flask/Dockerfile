ARG host_name
ARG user_name
ARG user_password
ARG db_name

FROM python:3-alpine3.15

ENV host_name=${host_name}
ENV user_name=${user_name}
ENV user_password=${user_password}
ENV db_name=${db_name}

WORKDIR /app
COPY . /app/
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python ./app.py ${host_name} ${user_name} ${user_password} ${db_name}