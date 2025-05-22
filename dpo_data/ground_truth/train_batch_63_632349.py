import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-21,0))
r=w0.workplane(offset=42/2).moveTo(-2,39).cylinder(42,61).union(w0.sketch().segment((-8,-28),(24,-100)).segment((63,-83)).segment((31,-10)).close().assemble().finalize().extrude(43))