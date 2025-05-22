import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-90,0))
r=w0.workplane(offset=181/2).cylinder(181,100)