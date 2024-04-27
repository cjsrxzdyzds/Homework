FROM ubuntu:latest
LABEL authors="oscar"

ENTRYPOINT ["top", "-b"]

FROM mysql:latest

ENV MYSQL_DATABASE=dbs
ENV MYSQL_ALLOW_EMPTY_PASSWORD=true

COPY kindle_reviews.json /var/lib/mysql-files/
COPY kindle_reviews.csv /var/lib/mysql-files/
COPY kindle_reviews_processed.json /var/lib/mysql-files/
COPY kindle_reviews_formatted.json /var/lib/mysql-files/