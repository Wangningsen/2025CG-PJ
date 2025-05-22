import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-12,0))
w1=cq.Workplane('ZX',origin=(0,26,0))
r=w0.workplane(offset=-78/2).moveTo(-2.5,54.5).box(75,91,78).union(w0.sketch().segment((-76,10),(-72,-100)).segment((25,-100)).segment((25,-63)).arc((67,7),(-15,14)).close().assemble().push([(-35,-40)]).circle(31,mode='s').finalize().extrude(3)).union(w1.sketch().segment((-35,42),(-21,42)).segment((-21,34)).segment((-34,34)).arc((32,59),(-35,42)).assemble().push([(-25.5,57)]).rect(9,26,mode='s').finalize().extrude(64))