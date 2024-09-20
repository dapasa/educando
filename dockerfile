FROM python:3.9-slim
WORKDIR /usr/src/app
COPY juego.py .
CMD ["python", "./juego.py"]
