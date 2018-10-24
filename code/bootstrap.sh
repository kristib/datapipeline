#!/bin/bash

aws s3 cp --recursive s3://testing-datapipe/code /home/hadoop && chmod u+x /home/hadoop/*.py
