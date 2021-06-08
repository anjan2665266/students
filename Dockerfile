# Install Python
FROM python:latest as api
RUN apt-get update && apt-get install -y --no-install-recommends nano sudo iputils-ping && rm -rf /var/lib/apt/lists/*

# Create folder code and copy all files
RUN mkdir /home/students
ADD requirements.txt /home/students
ADD . /home/students
WORKDIR /home/students
RUN ls -al
# Install Python
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt