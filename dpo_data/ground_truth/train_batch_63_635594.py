import cadquery as cq
w0=cq.Workplane('YZ',origin=(9,0,0))
w1=cq.Workplane('ZX',origin=(0,86,0))
r=w0.sketch().segment((-86,-20),(-75,-20)).arc((-85,19),(-75,56)).segment((-86,56)).close().assemble().finalize().extrude(16).union(w1.sketch().segment((-95,-100),(-77,-100)).segment((-77,-89)).segment((-89,-89)).segment((-89,41)).segment((-21,41)).arc((0,-2),(46,-16)).segment((46,-45)).segment((53,-45)).segment((53,-14)).arc((76,85),(-20,52)).segment((-95,52)).close().assemble().finalize().extrude(-71))