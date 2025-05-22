import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-6,0))
w1=cq.Workplane('XY',origin=(0,0,-46))
r=w0.sketch().segment((25,7),(32,7)).segment((33,-4)).segment((94,-2)).segment((93,7)).segment((100,7)).segment((100,28)).segment((93,28)).segment((92,39)).segment((31,36)).segment((31,28)).segment((25,28)).close().assemble().finalize().extrude(-22).union(w0.sketch().segment((-27,-15),(6,-39)).segment((30,-5)).segment((-2,18)).close().assemble().finalize().extrude(34)).union(w1.workplane(offset=-54/2).moveTo(-24,-11).box(2,6,54))