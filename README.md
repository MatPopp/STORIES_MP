# STORIES 

This repository contains some code that I created during my research-stay at the Acceleration Consortium in January 2025. Most of the code is not finalized but might well serve for further developments. 

## Disclaimer

* I used large single-file jupyter notebooks within this project due to time constraints. For anyone re-using this code I highly recommend extracting device-drivers / optimizers into python modules! 

## Content
### opentrons 
(this contains the most relevant scripts)
* soap_mixing.ipynb : Code for using an opentrons Flex robot to mix two liquids, measure their viscosities and optimize the mixing ratio with standard Bayesian Optimization for some target viscosity. 
* soap_mixing_1000ul_pipette.ipynb : same as soap_mixing.ipynb but calibration curves recorded with 1000 ul pipettes. These have a larger diameter at their opening an can therefore deal with higher viscosities. 
* soap_recycling_Bayes.ipynb : code modified for
    * (1) model-building phase: automatically builds a process-model including input-characterization, i.e. output prediction depending on measurements on the input (material).

    * (2) production-optimization phase: use the process-model for being able to optimize the same kind of process for fixed (but unknown!) input material with hopefully less iterations.

### openflexure
* some code to enhance contrast for camera streams produced with an open-flexure microscope

### CameraPi
* code to be used on a raspberry-pi with a camera
* uses the picamera2 library for interfacing with the camera and streaming to an http endpoint. -> convenient and quite fast transmission of camera images within a local network. 