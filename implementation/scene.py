from manim import *

import examples as ex
import anim_utils as au
import a_star as ast


class BasicExample(Scene):
    def construct(self):
        
        title = Title('The $A^*$ algorithm: A Simple Example')
        
        self.add(title)
        
        nx_graph = ex.c6_example()
        
        partitions = [['s'], ['a','c'], ['b','d'], ['t']]

        heuristic_labels_pos = { 's': LEFT,
                               'a': UP,
                               'b': UP,
                               'c': DOWN,
                               'd': DOWN,
                               't': RIGHT
                               }

        factory = au.AnimationFactory(nx_graph, partitions, heuristic_labels_pos, self)

        ast.a_star(nx_graph, 's', {'t'}, factory)

class HardExample(Scene):
    def construct(self):

        nx_graph = ex.cities_example()

        partitions = []

        heuristic_labels_pos = { 'wic': LEFT,
                                 'emp': UP,
                                 'tpk': RIGHT,
                                 'akc': DOWN,
                                 'lfk': RIGHT,
                                 'bton': DOWN,
                                 'jpn': LEFT,
                                 'bvl': DOWN,
                                 'kc': DOWN,
                                 'pbg': LEFT
                                }

        factory = au.AnimationFactory(nx_graph, partitions, heuristic_labels_pos, self)
        ast.a_star(nx_graph, 'lfk', {'bvl'}, factory)


