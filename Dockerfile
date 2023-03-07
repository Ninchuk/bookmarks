FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /bookmarks
COPY requirements.txt /bookmarks/
RUN pip install -r requirements.txt
COPY . /bookmarks/
RUN chmod +x /bookmarks/scripts/django/run_service.sh