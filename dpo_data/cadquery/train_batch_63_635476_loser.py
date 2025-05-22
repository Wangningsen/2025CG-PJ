import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-35))
w1=cq.Workplane('XY',origin=(0,0,-36))
r=w0.sketch().rect(104,104).push([(-27,-45)]).circle(11,mode='s').finalize().extrude(22).union(w1.workplane(offset=72/2).cylinder(72,100))