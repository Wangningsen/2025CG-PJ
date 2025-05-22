import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,44,0))
w1=cq.Workplane('ZX',origin=(0,72,0))
r=w0.sketch().circle(100).circle(84,mode='s').finalize().extrude(5).union(w1.workplane(offset=-144/2).moveTo(-12.5,1.5).box(127,163,144))