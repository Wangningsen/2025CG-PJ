import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,34))
r=w0.sketch().segment((-100,-8),(-97,-8)).arc((-95,-4),(-92,0)).arc((-93,12),(-82,18)).arc((-78,31),(-69,42)).segment((-100,42)).close().assemble().finalize().extrude(-69).union(w0.workplane(offset=-28/2).moveTo(72.5,-20).box(55,44,28))