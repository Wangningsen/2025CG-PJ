import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,28))
w1=cq.Workplane('YZ',origin=(-80,0,0))
r=w0.workplane(offset=7/2).moveTo(0,-11).cylinder(7,89).union(w1.workplane(offset=135/2).moveTo(17.5,-27).box(165,16,135))