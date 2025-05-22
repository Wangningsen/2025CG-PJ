import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-34))
w1=cq.Workplane('XY',origin=(0,0,-37))
r=w0.workplane(offset=-21/2).moveTo(-75,-81).cylinder(21,19).union(w0.workplane(offset=90/2).moveTo(39,39).cylinder(90,27)).union(w0.workplane(offset=90/2).moveTo(39,39).cylinder(90,55)).union(w1.workplane(offset=-18/2).moveTo(38.5,38.5).box(7,123,18))