import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,35,0))
r=w0.workplane(offset=-70/2).cylinder(70,100)