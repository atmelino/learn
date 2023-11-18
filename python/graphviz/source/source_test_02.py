
from graphviz import Source

path = 'graphviz/source/Neuron_01.gv'
s = Source.from_file(path)
print(s.source)
s.render('graphviz/source/Neuron_01.gv', format='jpg',view=True)