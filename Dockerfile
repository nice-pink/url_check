FROM python:3.8

# Info
LABEL org.opencontainers.image.authors="raffael@nice.pink"

# 
WORKDIR /app

# install dependencies
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

# Copy script
COPY url_check/ ./url_check

# Command
CMD [ "python", "-m", "url_check", "--config", "{\"urls\": [\"https://example.com\"]}" ]
