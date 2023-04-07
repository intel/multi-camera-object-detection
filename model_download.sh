#!/bin/bash

# Copyright (C) 2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

mkdir -p $HOME/multi-cam/models

mkdir -p $HOME/multi-cam/models/yolov5s/FP32
mkdir -p $HOME/multi-cam/models/yolov5s/FP16

mkdir -p $HOME/multi-cam/models/person-detection/FP32
mkdir -p $HOME/multi-cam/models/person-detection/FP16

wget -P $HOME/multi-cam/models/yolov5s/FP32 https://github.com/dlstreamer/pipeline-zoo-models/raw/main/storage/yolov5s-416/FP32/yolov5s.bin
wget -P $HOME/multi-cam/models/yolov5s/FP32 https://github.com/dlstreamer/pipeline-zoo-models/raw/main/storage/yolov5s-416/FP32/yolov5s.xml

wget -P $HOME/multi-cam/models/yolov5s/FP16 https://github.com/dlstreamer/pipeline-zoo-models/raw/main/storage/yolov5s-416/FP16/yolov5s.bin
wget -P $HOME/multi-cam/models/yolov5s/FP16 https://github.com/dlstreamer/pipeline-zoo-models/raw/main/storage/yolov5s-416/FP16/yolov5s.xml
wget -P $HOME/multi-cam/models/yolov5s https://raw.githubusercontent.com/dlstreamer/pipeline-zoo-models/main/storage/yolov5s-416/yolov5s.json

wget -P $HOME/multi-cam/models/person-detection/FP32 https://storage.openvinotoolkit.org/repositories/open_model_zoo/2022.3/models_bin/1/person-detection-retail-0013/FP32/person-detection-retail-0013.xml
wget -P $HOME/multi-cam/models/person-detection/FP32 https://storage.openvinotoolkit.org/repositories/open_model_zoo/2022.3/models_bin/1/person-detection-retail-0013/FP32/person-detection-retail-0013.bin

wget -P $HOME/multi-cam/models/person-detection/FP16 https://storage.openvinotoolkit.org/repositories/open_model_zoo/2022.3/models_bin/1/person-detection-retail-0013/FP16/person-detection-retail-0013.xml
wget -P $HOME/multi-cam/models/person-detection/FP16 https://storage.openvinotoolkit.org/repositories/open_model_zoo/2022.3/models_bin/1/person-detection-retail-0013/FP16/person-detection-retail-0013.bin

cp pipeline.py config.json $HOME/multi-cam/
