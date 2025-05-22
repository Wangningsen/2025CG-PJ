import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-51,0))
w1=cq.Workplane('XY',origin=(0,0,43))
r=w0.workplane(offset=-47/2).cylinder(47,88).union(w0.sketch().segment((-49,-31),(49,-31)).segment((49,31)).segment((-13,31)).arc((-18,32),(-23,31)).segment((-49,31)).close().assemble().finalize().extrude(151)).union(w1.workplane(offset=-122/2).moveTo(0,-28).cylinder(122,72))