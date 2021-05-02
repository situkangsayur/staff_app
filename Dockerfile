FROM ubuntu

ARG APP_NAME
ARG VERSION

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHON_VERSION=3.9
ENV TZ=Asia/Jakarta

COPY dist/$APP_NAME-$VERSION.tar.gz /opt/

RUN tar xfvz /opt/$APP_NAME-$VERSION.tar.gz -C /opt/ \ 
    && mv /opt/$APP_NAME-$VERSION /opt/$APP_NAME \
    && apt-get update \
    && apt-get purge python \
    && apt-get install -y apt-utils python$PYTHON_VERSION nginx python3-pip supervisor lynx telnet iputils-ping --no-install-recommends
        
ENV PYTHONPATH=$PYTHONPATH:/usr/local/lib/python$PYTHON_VERSION/site-packages:/usr/lib/python3.9/site-packages

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

COPY nginx_app /etc/nginx/sites-available


WORKDIR /opt/$APP_NAME

RUN apt-get clean && rm -rf /var/lib/apt/lists/* \
  && /usr/bin/python3 -m pip install --upgrade pip \ 
  && /usr/bin/python3 -m pip install virtualenv \
  && virtualenv -p python3 venv \
  && mkdir /opt/$APP_NAME/logs \
  && ls -l /opt/$APP_NAME \
  && . venv/bin/activate \
  && venv/bin/python3 -m pip install -r /opt/$APP_NAME/requirements.txt \ 
  && rm /opt/$APP_NAME-$VERSION.tar.gz \
  && rm /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default \
  && ln -sf /etc/nginx/sites-available/nginx_app /etc/nginx/sites-enabled/nginx_app


COPY logs /opt/$APP_NAME/logs

# RUN apt-get install -y libxml2-dev libxslt1-dev
#
CMD ["/usr/bin/supervisord"]

MAINTAINER TestingStaff
