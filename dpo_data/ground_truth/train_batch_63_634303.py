import cadquery as cq
w0=cq.Workplane('YZ',origin=(-68,0,0))
r=w0.workplane(offset=52/2).moveTo(-48,66).cylinder(52,11).union(w0.workplane(offset=62/2).moveTo(95,-82).cylinder(62,5)).union(w0.sketch().segment((-100,47),(3,47)).segment((3,87)).segment((-14,87)).segment((-100,87)).close().assemble().finalize().extrude(136))