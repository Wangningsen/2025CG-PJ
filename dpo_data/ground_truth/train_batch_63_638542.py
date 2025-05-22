import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,11))
w1=cq.Workplane('XY',origin=(0,0,5))
r=w0.workplane(offset=-71/2).moveTo(-52,-58).cylinder(71,42).union(w0.workplane(offset=-11/2).moveTo(59,-46).cylinder(11,35)).union(w0.workplane(offset=50/2).moveTo(15,44).cylinder(50,12)).union(w1.sketch().segment((38,94),(38,97)).arc((19,79),(40,95)).segment((40,94)).close().assemble().push([(22.5,87)]).rect(7,4,mode='s').push([(26,95)]).circle(1,mode='s').finalize().extrude(2))