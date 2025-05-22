import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,14))
r=w0.sketch().segment((-100,-75),(-8,-75)).segment((-8,-20)).arc((-5,-18),(-2,-15)).arc((92,-47),(28,24)).arc((-29,74),(-65,6)).segment((-100,6)).close().assemble().push([(-63,-16)]).circle(15,mode='s').finalize().extrude(-97).union(w0.workplane(offset=69/2).moveTo(51,-20).cylinder(69,36))