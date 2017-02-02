import logging
import importlib
import neuron_utils
from geppettoJupyter.geppetto_comm import GeppettoJupyterModelSync

from neuron import h

class SampleModels:
    def __init__(self):
        logging.debug('Initializing Samples panel')
        self.items = []
        self.items.append(neuron_utils.add_button('Single compartment Hodgkin-Huxley', self.loadModule, extraData = {'module': 'verysimple_cell', 'model':'VerySimpleCell'}))
        self.items.append(neuron_utils.add_button('Multi compartments Hodgkin-Huxley', self.loadModule, extraData = {'module': 'simple_cell', 'model':'SimpleCell'}))
        #self.items.append(neuron_utils.add_button('Simple network', self.loadModule, extraData = {'module': 'simple_network', 'model':'SimpleNetwork'}))
        self.items.append(neuron_utils.add_button('Ring network', self.loadModule, extraData = {'module': 'ring', 'model':'Ring'}))
        self.items.append(neuron_utils.add_button('CA3 Pyramidal', self.loadModule, extraData = {'module': 'CA3_pyramidal', 'model':'CA3_pyramidal'}))
        self.items.append(neuron_utils.add_button('PT Cell', self.loadModule, extraData = {'module': 'PTcell', 'model':'PTcell'}))

        self.loadModelPanel = neuron_utils.add_panel('Sample NEURON Models', items = self.items, widget_id = 'loadModelPanel', position_x =108, position_y=125, width = 287)
        self.loadModelPanel.display() 

    def loadModule(self, triggeredComponent, args):
        try:
            #FIXME: Not working when moving from CA3 Pyramidal to simple cell
            h('forall delete_section()')

            logging.debug('Loading model ' + triggeredComponent.extraData['module'])
            #FIXME: Check if it works in python 2
            module = importlib.import_module("models." + triggeredComponent.extraData['module'])
            GeppettoJupyterModelSync.current_python_model = getattr(module, triggeredComponent.extraData['model'])()

        except Exception as e:
            logging.exception("Unexpected error loading model")
            raise