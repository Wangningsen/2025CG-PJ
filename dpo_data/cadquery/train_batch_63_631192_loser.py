import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-3))
w1=cq.Workplane('ZX',origin=(0,-29,0))
r=w0.workplane(offset=103/2).moveTo(4.5,-7).box(99,30,103).union(w1.workplane(offset=58/2).moveTo(-89,-43).cylinder(58,11))