
# Copyright (C) 2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

import json
import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GObject, GLib

DL_MODEL1='"models/yolov5s/FP16/yolov5s.xml" model-proc="yolov5s/FP16/yolov5s.json"'
DL_MODEL2="models/person-detection/FP16/person-detection-retail-0013.xml"

with open("config.json") as file:
    config = json.load(file)

num_cam = config["number_cameras"]
cams = config["cam_url"]
display = config["display"]
target_device = config["inference_device"]
decode_element=""
params=""

if (target_device == "GPU"):
    target_device = "GPU"
    decode_element = "decodebin "
    params=" nireq=8 ! gvawatermark "
else:
    target_device="CPU"
    decode_element = "decodebin"
    params=" ! gvawatermark"

if (type(num_cam) == str):
    print(f"    \nnumber_cameras should only be integer value\n")
elif(num_cam > 8):
    print(f'Demo currently supportls 8 streams only')
else:
        composite_sinks = {
            1:"sink_1::alpha=1", 
            2:"sink_1::xpos=0 sink_2::xpos=640", 
            3:"sink_1::xpos=0 sink_2::xpos=640 sink_3::ypos=360", 
            4:"sink_1::xpos=0 sink_2::xpos=640 sink_3::ypos=360 sink_4::xpos=640 sink_4::ypos=360",
            5:"sink_1::xpos=0 sink_2::xpos=640 sink_3::ypos=360 sink_4::xpos=640 sink_4::ypos=360 sink_5::xpos=1280",
            6:"sink_1::xpos=0 sink_2::xpos=640 sink_3::ypos=360 sink_4::xpos=640 sink_4::ypos=360 sink_5::xpos=1280 sink_6::xpos=1280 sink_6::ypos=360",
            7:"sink_1::xpos=0 sink_2::xpos=640 sink_3::ypos=360 sink_4::xpos=640 sink_4::ypos=360 sink_5::xpos=1280 sink_6::xpos=1280 sink_6::ypos=360 sink_7::ypos=720",
            8:"sink_1::xpos=0 sink_2::xpos=640 sink_3::ypos=360 sink_4::xpos=640 sink_4::ypos=360 sink_5::xpos=1280 sink_6::xpos=1280 sink_6::ypos=360 sink_7::ypos=720 sink_8::xpos=640 sink_8::ypos=720"
            }
        scales = {
            1:"video/x-raw,width=1280,height=720", 
            2:"video/x-raw,width=640,height=480", 
            3:"video/x-raw,width=640,height=360", 
            4:"video/x-raw,width=640,height=360",
            5:"video/x-raw,width=640,height=360",
            6:"video/x-raw,width=640,height=360",
            7:"video/x-raw,width=640,height=360",
            8:"video/x-raw,width=640,height=360"
            }

        csink = composite_sinks[num_cam]
        dsink = ""

        pipeline=""
        
        if (display == "yes"):
            if(target_device=="GPU"):
                dsink = "videoconvert ! fpsdisplaysink video-sink=ximagesink sync=false"
            else:
                dsink = "videoconvert ! fpsdisplaysink video-sink=xvimagesink sync=false"
        else:
            dsink = "gvafpscounter ! fakesink async=false"

        def input_format(input):
            input = f'"{input}"'
            if ("/dev/video" in input):
                stream = "v4l2src device="+input
            elif ("://" in input):
                stream = "urisourcebin buffer-size=4096 uri=" +input
            else:
                stream = "filesrc location="+input
                
            return stream

        for i in range(num_cam):
            formatted_input = input_format(list(cams.values())[i])
            pipeline = pipeline + formatted_input + " ! " + decode_element + " ! gvadetect model="+DL_MODEL2+" device=" +target_device+ ""+params+ "" +" ! " + scales[num_cam] + " ! mix.sink_"+str(i+1) + " "

        final_pipeline = "compositor name=mix background=1 " + csink + " ! " + dsink + " " + pipeline
        print(final_pipeline)

        pipeline = None
        bus = None
        message = None
        
        Gst.init(None)
        pipeline = Gst.parse_launch(final_pipeline)

        # start playing
        pipeline.set_state(Gst.State.PLAYING)

        # wait until EOS or error
        bus = pipeline.get_bus()

        msg = bus.timed_pop_filtered(Gst.CLOCK_TIME_NONE, Gst.MessageType.ERROR | Gst.MessageType.EOS)

        pipeline.set_state(Gst.State.NULL)
