FROM python:slim
RUN mkdir -p /app
WORKDIR /app
RUN pip install flask
COPY templates/ /app/templates/
COPY flask-3.py /app
COPY startup.sh/ /app
RUN chmod +x /app/startup.sh
CMD ["/app/startup.sh"]
