import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-41,0))
w1=cq.Workplane('ZX',origin=(0,1,0))
r=w0.workplane(offset=102/2).moveTo(83.5,0).box(33,118,102).union(w1.sketch().segment((-100,-15),(-95,-15)).arc((-98,-5),(-100,5)).close().assemble().finalize().extrude(-62))