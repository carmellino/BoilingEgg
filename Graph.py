import graphviz
from Action import action

import cpm

class DrawGraph:

    def draw(actions):
        graph = graphviz.Digraph(format='png')
        graph.node_attr['shape']='circle'
        # generate path
        # y=1
        # for x in cpm.events:
        #     start = str(x.id)
        #
        #     graph.node(str(y), str(y))
        #     y += 1
        
        for x in actions:
            if x in cpm.critical:
                graph.edge(str(x.startingEvent.id), str(x.endingEvent.id), str(x.id), color='red')
            else:
                #action[x].startingEvent.id -> action[x].endingEvent.id ??
                graph.edge(str(x.startingEvent.id),str(x.endingEvent.id), str(x.id))
        print(graph.source)


        
        graph.render(directory='./test-output', view=False)
        # label edges