import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-27))
w1=cq.Workplane('XY',origin=(0,0,-24))
r=w0.sketch().push([(-15,66)]).rect(74,68).reset().face(w0.sketch().segment((-32,63),(-12,47)).segment((3,66)).segment((-17,84)).close().assemble(),mode='s').push([(15,40)]).circle(4,mode='s').finalize().extrude(-29).union(w0.workplane(offset=-4/2).moveTo(35,-11).box(34,32,4)).union(w1.workplane(offset=79/2).moveTo(-12,-64.5).box(50,71,79))