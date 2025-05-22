import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,80,0))
r=w0.workplane(offset=-160/2).box(100,200,160)