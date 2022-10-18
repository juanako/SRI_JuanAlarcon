#!/usr/bin/python3

import time

import os
import docker
client = docker.from_env()

image = 'httpd'
binding = {80: 8080}

print("Downloading Image...")
image = client.images.pull(image)
print(image.id)
time.sleep(3)
print("Image downloaded")
print("Running container..")
container = client.containers.run(image, detach=True, ports=binding)
print("Container started with ID: {}".format(container.id))
time.sleep(3)
print("Container running with the port binding " + str(binding))
