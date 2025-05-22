import cadquery as cq
w0=cq.Workplane('YZ',origin=(-22,0,0))
w1=cq.Workplane('XY',origin=(0,0,29))
r=w0.workplane(offset=-60/2).moveTo(27,37).cylinder(60,31).union(w1.workplane(offset=-98/2).moveTo(0,-17.5).box(200,81,98))