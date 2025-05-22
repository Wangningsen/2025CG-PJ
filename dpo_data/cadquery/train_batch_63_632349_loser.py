import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-21,0))
w1=cq.Workplane('ZX',origin=(0,21,0))
r=w0.sketch().segment((-11,-25),(24,-100)).segment((63,-83)).segment((28,-5)).close().assemble().finalize().extrude(43).union(w1.workplane(offset=-43/2).moveTo(-2,39).cylinder(43,61))