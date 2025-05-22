import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-29))
w1=cq.Workplane('ZX',origin=(0,4,0))
r=w0.sketch().arc((-8,77),(-65,8),(24,-4)).segment((61,-4)).segment((61,23)).arc((68,48),(61,72)).segment((61,100)).segment((-8,100)).close().assemble().finalize().extrude(-45).union(w1.workplane(offset=-104/2).moveTo(30,15.5).box(88,19,104))