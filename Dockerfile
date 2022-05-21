FROM docker.io/python:3.10-rc-alpine3.12

WORKDIR /app

COPY requirements.txt .

RUN \
    # These packages are needed to build lxml
    # The "--virtual" flag creates virtual package ".build-deps" which is not added to global packages and can be easily deleted
    apk add --no-cache --virtual .build-deps gcc musl-dev libxml2-dev libxslt-dev && \
    python3 -m pip install -r requirements.txt --no-cache-dir && \
    apk --purge del .build-deps


RUN apk add libxml2 libxslt

COPY . .

RUN python -m compileall

CMD ["python", "main.py"]
