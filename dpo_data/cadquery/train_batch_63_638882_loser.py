import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,9,0))
r=w0.workplane(offset=-18/2).box(200,148,18)