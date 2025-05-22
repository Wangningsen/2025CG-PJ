import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-48))
r=w0.sketch().push([(33,-32)]).circle(59).circle(41,mode='s').finalize().extrude(2).union(w0.sketch().segment((-92,-52),(-29,-52)).arc((62,-56),(-21,-19)).segment((-21,100)).segment((-92,100)).close().assemble().reset().face(w0.sketch().arc((-3,-52),(38,-43),(1,-27)).segment((1,-52)).close().assemble(),mode='s').finalize().extrude(96))