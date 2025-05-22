import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,34))
r=w0.sketch().segment((-100,-8),(-93,-8)).arc((-93,12),(-80,22)).segment((-69,42)).segment((-100,42)).close().assemble().finalize().extrude(-69).union(w0.workplane(offset=-28/2).moveTo(72.5,-20).box(55,44,28))