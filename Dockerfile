FROM jupyter/base-notebook:latest
USER root
RUN apt-get -qq update
RUN apt-get -y install unzip
RUN apt-get -y install libx11-dev
RUN apt-get -y install libxext-dev
RUN apt-get -y install mpich
RUN apt-get -y install libncurses-dev
RUN apt-get -y install git-core
RUN apt-get -y install g++
RUN apt-get -y install libncurses5-dev libncursesw5-dev
RUN apt-get -y install make
USER jovyan
RUN wget http://www.neuron.yale.edu/ftp/neuron/versions/v7.4/nrn-7.4.tar.gz
RUN tar xzvf nrn-7.4.tar.gz
WORKDIR nrn-7.4
RUN ./configure --prefix `pwd` --without-iv --with-nrnpython
RUN make
RUN make install
WORKDIR src/nrnpython
RUN python setup.py install
RUN wget https://github.com/MetaCell/NEURON-UI/archive/development.zip
RUN unzip development.zip
WORKDIR NEURON-UI-development/utilities
RUN python install.py
CMD exec jupyter notebook --debug --NotebookApp.default_url=/geppetto --NotebookApp.token=''
