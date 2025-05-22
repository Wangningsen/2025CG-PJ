import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-25,0))
r=w0.workplane(offset=50/2).cylinder(50,100)