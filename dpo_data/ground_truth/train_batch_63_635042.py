import cadquery as cq
w0=cq.Workplane('YZ',origin=(70,0,0))
r=w0.workplane(offset=-141/2).cylinder(141,100)