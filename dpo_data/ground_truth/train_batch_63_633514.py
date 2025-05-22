import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,46,0))
w1=cq.Workplane('XY',origin=(0,0,-72))
r=w0.sketch().segment((38,-7),(41,-7)).segment((42,-1)).arc((99,35),(64,93)).segment((65,99)).segment((62,100)).segment((61,94)).arc((4,57),(39,-1)).close().assemble().finalize().extrude(-93).union(w0.workplane(offset=-46/2).moveTo(-48.5,18).box(103,68,46)).union(w1.workplane(offset=52/2).moveTo(-44.5,8).box(111,50,52))