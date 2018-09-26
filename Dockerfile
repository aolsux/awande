FROM python:3.6-slim

# well this is unsafe.. I think we should use a dedicated user here :-D
# see e.g. https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#user

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./awande /awande
WORKDIR /awande

CMD ["python", "main.py"]
