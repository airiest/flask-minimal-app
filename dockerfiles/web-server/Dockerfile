FROM nginx:latest

RUN mkdir -p /etc/nginx /var/www/test
COPY config/nginx.conf /etc/nginx/nginx.conf

# 疎通テスト用
RUN echo "This is Test Page!!" > /var/www/test/index.html
