from graphviz import Source

path = 'graphviz/source/abcd.dot'
s = Source.from_file(path)
print(s.source)
    
s.render('graphviz/source/abcd.gv', format='jpg',view=True)