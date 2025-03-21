FROM ghcr.io/home-assistant/aarch64-base-python:3.11

RUN pip install flask RPi.GPIO

COPY fan_control.py /fan_control.py

CMD ["python3", "/fan_control.py"]
