from cProfile import label
from logging import critical
from turtle import color
import graphviz
from Action import action

import cpm

class DrawGraph:
    def draw(actions):
        graph = graphviz.Digraph(format='png')
        graph.attr(rankdir = 'LR')
        graph.node_attr['shape']='circle'

        
        for x in actions:
            if x in cpm.critical:
                graph.edge(str(x.startingEvent.id), str(x.endingEvent.id), str(x.id + " " + str(x.duration)), color='red')
            else:
                graph.edge(str(x.startingEvent.id),str(x.endingEvent.id), str(x.id + " " + str(x.duration)))

        
        label = "Ścieżka Krytyczna:"        
        for x in actions:
            if x in cpm.critical:
                duration = x.duration
                label=label+" "+(str(x.id))
                
        label += "  Czas trwania: "+ str(cpm.critical[0])
        graph.attr(label=label)
        graph.attr(fontsize='16', fontcolor='red')
        graph.unflatten

        print(graph.source)    
        graph.render(directory='./graphs', view=False)
