import cadquery as cq
w0=cq.Workplane('YZ',origin=(-50,0,0))
r=w0.workplane(offset=100/2).cylinder(100,100)