import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,52,0))
w1=cq.Workplane('ZX',origin=(0,53,0))
r=w0.workplane(offset=-105/2).moveTo(-81.5,66).box(15,68,105).union(w1.sketch().segment((-51,-41),(-27,-41)).arc((29,-100),(87,-41)).segment((89,-41)).segment((89,7)).segment((60,7)).arc((29,14),(-2,7)).segment((-51,7)).close().assemble().reset().face(w1.sketch().segment((-11,-4),(-10,-4)).arc((-10,-3),(-11,-2)).close().assemble(),mode='s').finalize().extrude(-73))