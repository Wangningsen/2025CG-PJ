import cadquery as cq
w0=cq.Workplane('YZ',origin=(6,0,0))
w1=cq.Workplane('ZX',origin=(0,63,0))
r=w0.workplane(offset=-106/2).moveTo(84,-68).cylinder(106,3).union(w0.sketch().segment((-87,5),(3,-18)).segment((26,78)).segment((-64,100)).close().assemble().reset().face(w0.sketch().segment((6,53),(13,50)).segment((14,52)).segment((7,55)).close().assemble(),mode='s').finalize().extrude(94)).union(w1.sketch().segment((-100,-62),(6,-62)).segment((6,5)).segment((-52,5)).arc((-68,18),(-84,5)).segment((-100,5)).close().assemble().finalize().extrude(-73))