FROM python:3 
WORKDIR /app

# EXPOSE 5000
COPY . .
RUN pip install -r requirements.txt && rm -rf /root/.cache
ENTRYPOINT ["python3","app.py"]


# docker build -t socket-server . 
# docker run -d -p 5000:5000 socket-server 
