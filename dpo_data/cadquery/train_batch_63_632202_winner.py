import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,30))
r=w0.sketch().segment((26,-11),(28,-66)).segment((50,-65)).segment((48,-10)).close().assemble().push([(37,-37)]).circle(4,mode='s').finalize().extrude(-96).union(w0.sketch().arc((-71,-15),(60,-83),(15,62)).arc((4,73),(-9,81)).segment((-9,100)).segment((-58,100)).segment((-58,81)).arc((-90,42),(-71,-15)).assemble().finalize().extrude(35))