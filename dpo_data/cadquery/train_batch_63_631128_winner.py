import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,62,0))
w1=cq.Workplane('XY',origin=(0,0,63))
r=w0.workplane(offset=23/2).moveTo(-94,64).cylinder(23,6).union(w1.workplane(offset=37/2).moveTo(-31,-81.5).box(78,7,37))