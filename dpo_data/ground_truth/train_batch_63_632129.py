import cadquery as cq
w0=cq.Workplane('YZ',origin=(74,0,0))
w1=cq.Workplane('XY',origin=(0,0,20))
r=w0.workplane(offset=26/2).moveTo(2.5,0.5).box(105,77,26).union(w1.workplane(offset=-60/2).moveTo(-49,-4).cylinder(60,51))