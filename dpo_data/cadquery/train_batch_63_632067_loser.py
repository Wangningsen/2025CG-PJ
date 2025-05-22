import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,39,0))
r=w0.workplane(offset=-78/2).cylinder(78,100)