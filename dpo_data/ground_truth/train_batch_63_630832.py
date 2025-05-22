import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-100,0))
r=w0.workplane(offset=200/2).box(112,16,200)