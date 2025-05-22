import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,21,0))
w1=cq.Workplane('XY',origin=(0,0,22))
r=w0.sketch().segment((-13,-11),(-13,-2)).arc((-21,-8),(-13,-11)).assemble().finalize().extrude(-83).union(w0.sketch().segment((-100,-14),(-41,-14)).segment((-41,-2)).segment((-12,-2)).segment((-12,14)).segment((-100,14)).close().assemble().finalize().extrude(-76)).union(w1.workplane(offset=78/2).moveTo(-9,58).cylinder(78,4))