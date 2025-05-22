import cadquery as cq
w0=cq.Workplane('YZ',origin=(-83,0,0))
r=w0.workplane(offset=147/2).moveTo(80.5,33.5).box(39,25,147).union(w0.sketch().segment((-88,-4),(-68,-4)).segment((-68,28)).segment((-87,28)).arc((-31,-37),(-88,27)).close().assemble().finalize().extrude(167))