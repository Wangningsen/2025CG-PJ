import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-12,0))
r=w0.workplane(offset=24/2).box(36,200,24)