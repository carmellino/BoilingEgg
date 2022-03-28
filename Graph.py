import graphviz
from Action import action

class DrawGraph:

    def draw(actions):
        graph = graphviz.Digraph(format='png')
        graph.node_attr['shape']='circle'
        # generate path
        y=1
        for x in actions:
            start = str(x.id)
            
            graph.node(str(y),str(y))
            y+=1
        
        for x in actions:
            #action[x].startingEvent.id -> action[x].endingEvent.id ??
            graph.edge(str(x.startingEvent.id),str(x.endingEvent.id), str(x.id))
        print(graph.source)


        
        graph.render(directory='./test-output', view=True)
        # label edges