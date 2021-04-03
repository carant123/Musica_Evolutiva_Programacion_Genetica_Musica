#from util import rttl
from mingus.containers import Track
import rttl1

class song(object):
    def __init__(self,
                 genome,
                 evolution,
                 generation,
                 individual_id,
                 parent_1 = '',
                 parent_2 = '',
                 grade = 0.0,
                 status = 'created'):

        
        self.evolution = evolution
        self.generation = generation
        self.parent_1 = parent_1
        self.parent_2 = parent_2
        self.grade = grade
        self.status = status
        self.individual_id = individual_id

        self.set_genome(genome)

        self.mingus_track = Track()
        
        for n in self.note_list:
            self.mingus_track.add_notes(n.mingus_note, n.mingus_duration)

        self.name = self.evolution + '-' + str(self.generation) + '-' + str(self.individual_id)
        return

    @property
    def selected(self):
        return self.status == 'selected'

    def set_genome(self, genome):
        if type(genome) is list:
            self.note_list = genome
            self.genome = rttl1.dump(genome)

        elif type(genome) is unicode:
            self.genome = genome
            self.note_list = rttl1.parse(genome)

        self.int_list = rttl1.to_int(self.note_list)

