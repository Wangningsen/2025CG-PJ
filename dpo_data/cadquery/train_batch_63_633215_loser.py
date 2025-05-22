import cadquery as cq
w0=cq.Workplane('YZ',origin=(4,0,0))
w1=cq.Workplane('XY',origin=(0,0,60))
r=w0.workplane(offset=96/2).cylinder(96,97).union(w1.workplane(offset=-84/2).moveTo(-80.5,10.5).box(39,71,84))