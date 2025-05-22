import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-19))
w1=cq.Workplane('ZX',origin=(0,-40,0))
r=w0.workplane(offset=54/2).moveTo(-50,55).cylinder(54,26).union(w0.workplane(offset=119/2).moveTo(39,-43).cylinder(119,38)).union(w1.workplane(offset=112/2).moveTo(-95,-50).box(10,54,112))