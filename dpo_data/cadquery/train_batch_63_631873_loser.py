import cadquery as cq
w0=cq.Workplane('YZ',origin=(10,0,0))
r=w0.workplane(offset=-20/2).cylinder(20,100)