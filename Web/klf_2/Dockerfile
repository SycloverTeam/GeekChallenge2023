FROM python:3.6

WORKDIR /app
COPY . .


RUN pip install Flask==1.1.1 -i  https://pypi.tuna.tsinghua.edu.cn/simple
RUN chmod +x /app/replace.sh 
RUN chmod 700 /app/hello/ssti/app.py

EXPOSE 7889
WORKDIR /app/hello/ssti
CMD ["/bin/sh", "/app/replace.sh"]


