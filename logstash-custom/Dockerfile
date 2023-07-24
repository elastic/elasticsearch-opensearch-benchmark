FROM docker.elastic.co/logstash/logstash:8.8.2

USER root

RUN apt-get update && \
    apt-get install -y shared-mime-info && \
    apt-get clean

USER logstash
RUN /usr/share/logstash/bin/ruby -S gem install mimemagic -v '>= 0.3.7'

WORKDIR /usr/share/logstash

RUN bin/logstash-plugin install logstash-input-google_cloud_storage
RUN bin/logstash-plugin install logstash-output-opensearch

