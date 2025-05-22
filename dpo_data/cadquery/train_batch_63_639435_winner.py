import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,44,0))
w1=cq.Workplane('ZX',origin=(0,72,0))
r=w0.sketch().circle(100).reset().face(w0.sketch().segment((-38,5),(-27,-22)).segment((38,-5)).segment((27,22)).close().assemble(),mode='s').finalize().extrude(5).union(w1.workplane(offset=-144/2).moveTo(-12.5,1.5).box(127,163,144))