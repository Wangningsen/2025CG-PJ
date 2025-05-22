import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-94,0))
r=w0.workplane(offset=189/2).cylinder(189,100)