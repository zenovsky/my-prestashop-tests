FROM python:3.11-slim

WORKDIR /workspace

RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    gnupg \
    firefox-esr \
    chromium \
    chromium-driver \
    default-jre \
    && rm -rf /var/lib/apt/lists/*

RUN wget https://github.com/allure-framework/allure2/releases/download/2.30.0/allure-2.30.0.tgz && \
    tar -zxvf allure-2.30.0.tgz -C /opt/ && \
    ln -s /opt/allure-2.30.0/bin/allure /usr/bin/allure && \
    rm allure-2.30.0.tgz

RUN pip install --upgrade pip

ENV PYTHONUNBUFFERED=1