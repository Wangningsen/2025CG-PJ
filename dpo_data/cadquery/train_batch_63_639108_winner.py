import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,34))
r=w0.sketch().segment((-100,-8),(-95,-8)).arc((-94,-2),(-92,1)).arc((-93,12),(-83,18)).arc((-77,33),(-69,42)).segment((-100,42)).close().assemble().finalize().extrude(-69).union(w0.workplane(offset=-28/2).moveTo(72.5,-20).box(55,44,28))