import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-40))
r=w0.workplane(offset=57/2).moveTo(2,-79).cylinder(57,21).union(w0.workplane(offset=80/2).moveTo(-13.5,84).box(19,32,80))