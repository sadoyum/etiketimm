FROM python:3.9.10

WORKDIR /Plugins 
COPY . /Plugins 
 
RUN pip3 install -U pip
COPY requirements.txt .
RUN pip3 install -U -r requirements.txt

CMD ["python3", "-m", "Plugins"]
