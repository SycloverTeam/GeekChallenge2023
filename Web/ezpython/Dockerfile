FROM python

COPY ./src /app/
COPY start.sh /

RUN pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple

RUN pip install -r /app/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple 

RUN chmod -R 777 /start.sh

ENTRYPOINT ./start.sh

EXPOSE 8888

