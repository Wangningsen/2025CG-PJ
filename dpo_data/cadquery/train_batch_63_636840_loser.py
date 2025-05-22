import cadquery as cq
w0=cq.Workplane('YZ',origin=(68,0,0))
r=w0.workplane(offset=-137/2).cylinder(137,100)