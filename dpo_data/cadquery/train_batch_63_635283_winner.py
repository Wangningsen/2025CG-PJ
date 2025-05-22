import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-31))
r=w0.sketch().push([(-37,-44)]).circle(56).reset().face(w0.sketch().segment((-15,75),(-4,71)).segment((-4,49)).segment((76,49)).segment((86,46)).segment((93,70)).segment((82,73)).segment((82,97)).segment((3,97)).segment((-7,100)).close().assemble()).push([(39,72.5)]).rect(8,41,mode='s').finalize().extrude(62)