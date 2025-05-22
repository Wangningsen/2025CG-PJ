import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,48,0))
r=w0.workplane(offset=-96/2).cylinder(96,100)