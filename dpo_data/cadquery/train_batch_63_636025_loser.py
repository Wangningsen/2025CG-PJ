import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-54,0))
w1=cq.Workplane('ZX',origin=(0,-58,0))
r=w0.workplane(offset=-46/2).moveTo(30,-72).box(130,44,46).union(w0.workplane(offset=51/2).moveTo(-38,37).cylinder(51,57)).union(w0.workplane(offset=154/2).moveTo(-37,39).cylinder(154,42)).union(w1.sketch().segment((-33,66),(-27,66)).arc((-25,77),(-21,87)).segment((-33,87)).close().assemble().finalize().extrude(158))