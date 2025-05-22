import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,21,0))
w1=cq.Workplane('XY',origin=(0,0,22))
r=w0.workplane(offset=-83/2).moveTo(-17,-7).cylinder(83,4).union(w0.sketch().segment((-100,-14),(-41,-14)).segment((-41,-2)).segment((-12,-2)).segment((-12,14)).segment((-100,14)).close().assemble().finalize().extrude(-76)).union(w1.sketch().arc((-12,61),(-6,56),(-10,62)).arc((-10,61),(-12,61)).assemble().finalize().extrude(78))