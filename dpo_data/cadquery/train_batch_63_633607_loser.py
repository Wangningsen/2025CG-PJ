import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-8,0))
w1=cq.Workplane('XY',origin=(0,0,46))
r=w0.workplane(offset=-31/2).moveTo(-66,-35).cylinder(31,34).union(w0.sketch().push([(61,30)]).circle(39).circle(6,mode='s').finalize().extrude(79)).union(w1.sketch().segment((-3,-71),(-1,-71)).segment((-1,-38)).arc((15,0),(-3,-37)).close().assemble().push([(0,-33)]).circle(6,mode='s').finalize().extrude(-56))