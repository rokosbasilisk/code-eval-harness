FROM python:3
COPY . ./data
RUN pip install --no-cache-dir -r ./data/requirements.txt
EXPOSE 5000
CMD [ "python", "./data/server.py" ]


