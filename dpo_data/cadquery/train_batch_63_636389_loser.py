import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-55,0))
w1=cq.Workplane('XY',origin=(0,0,22))
r=w0.sketch().segment((-22,-10),(-17,-11)).segment((-17,-10)).segment((-16,-11)).segment((-17,-11)).segment((-17,-2)).segment((-12,-2)).segment((-12,14)).segment((-22,14)).close().assemble().finalize().extrude(-7).union(w0.sketch().segment((-100,-14),(-41,-14)).segment((-41,-2)).segment((-12,-2)).segment((-12,14)).segment((-100,14)).close().assemble().finalize().extrude(76)).union(w1.workplane(offset=78/2).moveTo(-9,58).cylinder(78,4))