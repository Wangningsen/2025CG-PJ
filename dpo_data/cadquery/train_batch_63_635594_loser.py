import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,86,0))
w1=cq.Workplane('XY',origin=(0,0,56))
r=w0.sketch().segment((-95,-100),(-77,-100)).arc((-78,-94),(-79,-89)).segment((-89,-89)).segment((-89,41)).segment((-20,41)).arc((0,-1),(46,-16)).segment((46,-45)).arc((50,-34),(53,-23)).segment((53,-14)).arc((77,84),(-20,52)).segment((-95,52)).close().assemble().finalize().extrude(-71).union(w1.workplane(offset=-77/2).moveTo(17.5,-81.5).box(15,9,77))