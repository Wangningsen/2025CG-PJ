import cadquery as cq
w0=cq.Workplane('YZ',origin=(-54,0,0))
r=w0.workplane(offset=109/2).cylinder(109,100)