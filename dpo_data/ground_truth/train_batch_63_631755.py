import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-30))
r=w0.sketch().segment((-100,-4),(-77,-16)).segment((-77,-27)).segment((-33,-27)).segment((-33,22)).segment((-30,26)).segment((-33,28)).segment((-33,33)).segment((-43,33)).segment((-71,49)).close().assemble().reset().face(w0.sketch().segment((49,3),(87,-41)).arc((31,7),(100,-18)).segment((68,20)).close().assemble()).finalize().extrude(61)