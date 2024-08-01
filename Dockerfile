# escape-room-lab/Dockerfile
FROM ubuntu:24.04
RUN apt-get update && apt-get install -y postgresql-client-16 apache2 iputils-ping curl
RUN echo "Hello, World!" > /var/www/html/index.html
COPY data/data2.csv /usr/share/
EXPOSE 80
CMD ["sleep", "infinity"]
