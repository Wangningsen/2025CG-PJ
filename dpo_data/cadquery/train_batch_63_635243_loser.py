import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,30,0))
r=w0.workplane(offset=-60/2).cylinder(60,100)