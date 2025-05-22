import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,52,0))
r=w0.workplane(offset=-105/2).moveTo(-81.5,66).box(15,68,105).union(w0.sketch().segment((-51,-41),(-27,-41)).arc((30,-100),(87,-41)).segment((89,-41)).segment((89,7)).segment((59,7)).arc((23,13),(-11,-4)).arc((-8,2),(-3,7)).segment((-51,7)).close().assemble().finalize().extrude(-72))