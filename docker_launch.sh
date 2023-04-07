#!/bin/bash

# Copyright (C) 2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

sudo docker run -t -d --rm --name dls -w /mnt -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY="$DISPLAY" -e XDG_RUNTIME_DIR=/tmp -v $HOME/multi-cam:/mnt --device /dev/dri:/dev/dri --group-add="$(stat -c "%g" /dev/dri/render*)" intel/dlstreamer:latest
