import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,74,0))
r=w0.workplane(offset=-148/2).cylinder(148,100)