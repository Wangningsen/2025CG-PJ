import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-30))
r=w0.sketch().segment((-100,-4),(-77,-16)).segment((-77,-27)).segment((-33,-26)).segment((-33,26)).segment((-30,26)).segment((-71,49)).close().assemble().reset().face(w0.sketch().arc((87,-41),(62,-12),(100,-18)).arc((30,6),(87,-41)).assemble()).push([(67,20)]).circle(2,mode='s').finalize().extrude(60)