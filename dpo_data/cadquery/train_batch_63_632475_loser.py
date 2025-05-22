import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,7,0))
w1=cq.Workplane('XY',origin=(0,0,0))
r=w0.workplane(offset=-70/2).moveTo(68,60.5).box(6,79,70).union(w0.workplane(offset=-3/2).moveTo(47,-76).cylinder(3,11)).union(w0.workplane(offset=56/2).moveTo(3,-78).cylinder(56,22)).union(w1.sketch().push([(-77.5,14)]).rect(45,36).push([(-78,14)]).circle(6,mode='s').finalize().extrude(-71))