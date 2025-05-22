import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-56,0))
r=w0.workplane(offset=113/2).box(200,64,113)