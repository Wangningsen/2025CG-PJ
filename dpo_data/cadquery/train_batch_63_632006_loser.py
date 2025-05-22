import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,31))
r=w0.sketch().push([(7,-72)]).circle(28).circle(4,mode='s').finalize().extrude(-62).union(w0.workplane(offset=-22/2).moveTo(-2,67).cylinder(22,33))