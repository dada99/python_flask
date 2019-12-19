FROM python:slim
RUN mkdir -p /app
WORKDIR /app
COPY requirements.txt ./
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install --no-cache-dir -r requirements.txt
COPY templates/ /app/templates/
COPY flask-3.py /app
COPY startup.sh/ /app
RUN chmod +x /app/startup.sh
EXPOSE 5000
CMD ["/bin/sh","-c","/app/startup.sh"]
