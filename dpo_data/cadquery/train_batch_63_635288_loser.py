import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-91,0))
r=w0.workplane(offset=182/2).cylinder(182,100)