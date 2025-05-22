import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,17))
r=w0.workplane(offset=-98/2).moveTo(-65.5,85).box(21,30,98).union(w0.sketch().segment((47,-100),(63,-100)).segment((63,-62)).arc((-28,19),(47,-76)).close().assemble().finalize().extrude(64))