FROM python:3.7
ADD . /nlp_app
WORKDIR /nlp_app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "app.py"]
