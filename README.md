# DISCONTINUATION OF PROJECT #  
This project will no longer be maintained by Intel.  
Intel has ceased development and contributions including, but not limited to, maintenance, bug fixes, new releases, or updates, to this project.  
Intel no longer accepts patches to this project.  
 If you have an ongoing need to use this project, are interested in independently developing it, or would like to maintain patches for the open source software community, please create your own fork of this project.  
  
## Reference demo/implementation for Devkits
> Multi Camera Object detection demo using DLStreamer + OpenVINO
   - DLStreamer - https://github.com/dlstreamer/dlstreamer

## Pre-Requisites 
 - Intel based Atom or Core systems
 - Ubuntu 22.04 LTS or 20.04 LTS
 - Intel GPU Enabled - Recommended to install Edge Insights for Vision from here (https://edgesoftware.intel.com/visioninsights) in order to install drivers and enable Intel GPU's seamlessly
 - Docker CE Installed - https://docs.docker.com/engine/install/ubuntu/
  
## Steps to run the sample
```
git clone https://github.com/intel/multi-camera-object-detection.git $HOME/multi-cam
```
Navigate into the repo and run scripts as below   
__NOTE: please download any sample videos into the multi-cam folder and give the same path in config.json before running demo__
  
```shell
$ ./model_download.sh
$ ./docker_launch.sh
$ ./run_milti_cam.sh
```
- You can use config.json file to modify options as below
   - num_cam - number of cameras/streams you want to process for inference
   - Inference device - Inference target device can be CPU or GPU (only works if you have enabled/installed iGPU drivers, refer Pre-Requisites section)
   - display - display output to screen (yes or no)

## Known Issues
- If device=GPU, some times you may encounter X Window Error
   - In this case you can ignore and execute "run_multi_cam.sh" script again

__NOTE: If you have any quries regarding this project, please use github issues__


