#!/bin/bash

docker build -t alexeysverchkov/online_inference:1.0.0 .
docker run -p 5432:5432 alexeysverchkov/online_inference:1.0.0