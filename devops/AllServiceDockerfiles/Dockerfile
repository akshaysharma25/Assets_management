FROM python:3.9.7-slim-buster
LABEL desc="This image is for course service"
LABEL author="rohit.singh@gslab.com"
ENV APP_HOME=/home/ubuntu
ENV APP_USER=ubuntu

RUN groupadd -r $APP_USER && \
    useradd -r -g $APP_USER -d $APP_HOME -s /sbin/nologin -c "Docker image user" $APP_USER

# define working dir
WORKDIR /home/ubuntu/assets_management_service

# copy application code & versions & release-notes
COPY  assets_management_service/ .

# install required python modules
RUN pip install -r requirements.txt

# copy entrypoint
COPY entrypoint.sh ./entrypoint.sh

RUN chown -R $APP_USER:$APP_USER $APP_HOME
USER $APP_USER

#start the Django server
EXPOSE 8000
ENTRYPOINT ["sh", "./entrypoint.sh"]

