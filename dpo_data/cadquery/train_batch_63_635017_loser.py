import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-3))
w1=cq.Workplane('ZX',origin=(0,-7,0))
r=w0.workplane(offset=103/2).moveTo(72,0).cylinder(103,17).union(w1.sketch().push([(-18.5,-16)]).rect(163,148).rect(11,50,mode='s').finalize().extrude(14))