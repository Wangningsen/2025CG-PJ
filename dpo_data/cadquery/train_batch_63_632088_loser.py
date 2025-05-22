import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-26))
w1=cq.Workplane('XY',origin=(0,0,-27))
r=w0.workplane(offset=53/2).moveTo(-59,-1).cylinder(53,41).union(w1.workplane(offset=54/2).moveTo(73,15).cylinder(54,27))