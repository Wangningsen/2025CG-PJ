import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,77,0))
r=w0.workplane(offset=-154/2).cylinder(154,100)