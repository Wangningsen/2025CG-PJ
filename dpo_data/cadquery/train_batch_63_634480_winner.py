import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,53,0))
r=w0.workplane(offset=-106/2).moveTo(-81.5,66).box(15,68,106).union(w0.sketch().segment((-51,-41),(-27,-41)).arc((26,-100),(87,-41)).segment((89,-41)).segment((89,7)).segment((59,7)).arc((29,14),(1,5)).segment((-4,0)).segment((-11,-4)).segment((-8,1)).arc((-10,3),(-11,7)).segment((-51,7)).close().assemble().finalize().extrude(-73))