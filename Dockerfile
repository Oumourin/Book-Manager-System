FROM frolvlad/alpine-python3 
EXPOSE 8080
WORKDIR /app
COPY . /app
RUN echo -e "https://mirrors.ustc.edu.cn/alpine/latest-stable/main\nhttps://mirrors.ustc.edu.cn/alpine/latest-stable/community" > /etc/apk/repositories
RUN apk --update --no-cache --wait 30 add py3-gevent
RUN pip3 install -r requirements.txt --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple
ENTRYPOINT ["/usr/bin/python3", "run-production.py"]


