import cadquery as cq
w0=cq.Workplane('YZ',origin=(-6,0,0))
r=w0.workplane(offset=-69/2).moveTo(45,11).cylinder(69,55).union(w0.sketch().segment((-43,-40),(-43,-35)).segment((-28,-35)).arc((-98,-18),(-29,-40)).close().assemble().finalize().extrude(82))