FROM ubuntu:18.04

LABEL maintainer="wentang@luminesence.jp"
LABEL version="1.0"
LABEL description="Unique ID: Snowflake ID & UUID"

# ENVs
ENV DEBIAN_FRONTEND=noninteractive
ENV LOCAL_DATA_FOLDER ./app
ENV SRC_DIR /app
ENV FILE_PIP_REQUIREMENTS requirements.txt
ENV START_SERVICE_FILE runapp.sh

# Copy files
COPY ${LOCAL_DATA_FOLDER} ${SRC_DIR}

WORKDIR ${SRC_DIR}
# Prepare Env & Instalation
RUN apt-get update -y \
    && apt-get install -y python3-pip \
    && pip3 install --upgrade pip \
    && chmod +x /app/runapp.sh \
    # RUN apt-get install -y python3
    && pip3 install --no-cache-dir "fastapi[all]" \
    && pip3 install --no-cache-dir "uvicorn[standard]"
    # && pip install -r requirements.txt


# Start service
EXPOSE 8105
CMD sh ${START_SERVICE_FILE}
