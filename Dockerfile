FROM python:3.9-slim-buster

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY get_last_posts.py README.md /app/

CMD ["python", "get_last_posts.py"]
