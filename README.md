
[![Build Status](https://travis-ci.org/MetaCell/NEURON-UI.svg?branch=master)](https://travis-ci.org/MetaCell/NEURON-UI)
[![Docker Automated buil](https://img.shields.io/docker/automated/jrottenberg/ffmpeg.svg)](https://hub.docker.com/r/metacell/neuron-ui/)

# NEURON-UI

This repository hosts an experimental prototype for a new user interface for [NEURON](http://www.neuron.yale.edu/neuron/) based on web technologies. 


![Screenshot](https://github.com/tarelli/bucket/raw/master//release034.png)

#### Install using Docker (self-contained, the simplest)

First install [Docker from here](https://www.docker.com/community-edition).

##### Install NEURON-UI using Docker graphical interface (Kitematic)
Open Kitematic from Docker menu (will install Kitematic if you don't have it already)

Search for neuron-ui and create the container.

![Image](https://github.com/tarelli/bucket/raw/master//neuronuiImage.png)

Start the container and click on Web preview to launch it. No need to ever use the command line, enjoy!

![Kitematic](https://github.com/tarelli/bucket/raw/master//kitematic.png)

##### Install NEURON-UI using Docker from command line 
```
docker pull metacell/neuron-ui
docker run -it -p 8888:8888 metacell/neuron-ui
```
Open your browser and connect to http://localhost:8888/geppetto.


#### Install NEURON-UI using pip
```
pip install neuron_ui
jupyter nbextension enable --py jupyter_geppetto
NEURON-UI
```

#### Install from sources (for developers and for using your own NEURON models)
```
git clone https://github.com/MetaCell/NEURON-UI.git
cd utilities
python install.py
cd ..
./NEURON-UI
```
##### To update sources:
```
python update.py
```

The available functionality is currently limited to the RunControl panel, a basic cell builder, a simplified point process manager that lets you inject a current clamp and space plot functionality.

![oldNEURON](https://github.com/tarelli/bucket/raw/master/Screen_Shot_2016-06-15_at_18.06.16.png)

This prototype is being developed in collaboration with the [Neurosim Lab](http://neurosimlab.org/) and the [Sense Lab](https://senselab.med.yale.edu/).

The UI connects to [nrnpython](http://www.neuron.yale.edu/neuron/static/docs/help/neuron/neuron/classes/python.html) through a [Geppetto](http://git.geppetto.org) extension for [Jupyter Notebook](http://jupyter.org/).

See the [Wiki](https://github.com/MetaCell/NEURON-UI/wiki) for more info!
