# Dockerfile, Image, Container
# Dockerfile is a blueprint for the image
# Image is a template to run the container
# Container is the actual running process where we have package project

From python:2.7
COPY . .
RUN pip install -r requirement.txt
CMD ["python", "/src/RBAC.py"]