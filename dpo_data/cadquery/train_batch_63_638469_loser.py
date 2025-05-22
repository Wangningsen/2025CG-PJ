import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-50,0))
r=w0.workplane(offset=100/2).cylinder(100,100)