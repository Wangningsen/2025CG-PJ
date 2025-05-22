import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-78,0))
r=w0.workplane(offset=157/2).box(200,12,157)