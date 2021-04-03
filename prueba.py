#!/usr/bin/python2.6

import sys, traceback
#import gtk
from src.evolution.brain.NN import neural_network
from src.evolution.manager import evolution
#import fluidsynth
#import pyFluidSynth

#from mingus.midi import fluidsynth
from src.util.storage import db
from src.constants import MIDI_FILE


class evolution9_app(object):
    def __init__(self):
        self.store = db()
        self.nn_list=[]
        #self.evolution9=""
        self.console = ""
        
        self.update_nn_list()

        self.on_new_neural_network()

        self.update_evolution_list()

        self.on_new_evolution()

        self.on_step_50()

        #self.on_new_evolution

        
        
    def update_nn_list(self):
        #self.nn_list.clear()
        networks = neural_network.get_list(self.store)
        print('networks=',networks)

        if networks:
            for n in networks:
                #self.nn_combo.append_text(n)
                print(n)
                

        return

    def on_new_neural_network(self):
        nn_name = 'red1'
        ds_file_uri = 'inputs/beatles.txt'

        try:
            neural_network.new(nn_name, self.store, ds_file_uri)
        except Exception as err:
            print(str(err))
            traceback.print_exc(file=sys.stdout)
        else:
            print('created neural network ', nn_name)
            self.update_nn_list()
            #self.new_neural_network_dialog.hide()

    def update_evolution_list(self):
        #self.evolution_list.clear()
        evolutions = evolution.get_list(self.store)
        print('evol',evolutions)
        if evolutions:
            for e in evolutions:
                print('evolutions',e)
                #self.evolution_combo.append_text(e)

        return

    def on_new_evolution(self):
        name = 'evolucion1'
        population_size = '20'
        evaluator = 'red1'

        try:
            self.evolution9 = evolution(name, evaluator, int(population_size), self.store)
        except Exception as err:
            print(str(err))
            traceback.print_exc(file=sys.stdout)
        else:
            #self.new_evolution_dialog.hide()
            self.start_evolution()


    def start_evolution(self):
        if self.evolution9.initialized:
            self.evolution9.reproduce(None)

        else:
            self.evolution9.initialized
        #self.update_state()
        #self.update_genome_list()

        print('is started', self.evolution9.name)



   
    def on_step_50(self):
        if not self.evolution9.initialized:
            self.evolution9.initialize()
        if self.evolution9.state == 'evaluate':
            self.evolution9.evaluate()
        if self.evolution9.state == 'select':
            self.evolution9.apply_selection(None)

        for _ in range(5):
            self.evolution9.reproduce()
            self.evolution9.evaluate()
            self.evolution9.apply_selection()

        #self.update_state()
        #self.update_genome_list()
        self.update_generation_info()

        return


    def update_generation_info(self):

        max_grade = "%.5f" % ( self.evolution9.max_grade )
        min_grade = "%.5f" % ( self.evolution9.min_grade )
        avg_grade = "%.5f" % ( self.evolution9.avg_grade )

        print('max_grade_label',max_grade)
        print('min_grade_label',min_grade)
        print('average_grade_label',avg_grade)


if __name__ == '__main__':
    app = evolution9_app()
    #app.main()
       