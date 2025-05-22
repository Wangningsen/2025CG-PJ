import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,11))
w1=cq.Workplane('XY',origin=(0,0,10))
r=w0.workplane(offset=-72/2).moveTo(-52,-58).cylinder(72,42).union(w0.sketch().push([(30,87)]).circle(13).push([(30.5,87)]).rect(17,2,mode='s').finalize().extrude(-6)).union(w0.workplane(offset=49/2).moveTo(15,44).cylinder(49,12)).union(w1.workplane(offset=-10/2).moveTo(59,-46).cylinder(10,35))