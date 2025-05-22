import cadquery as cq
w0=cq.Workplane('YZ',origin=(70,0,0))
r=w0.workplane(offset=-140/2).cylinder(140,46).union(w0.sketch().segment((-32,-100),(32,-100)).segment((32,-33)).arc((46,0),(32,33)).segment((32,100)).segment((-32,100)).segment((-32,55)).arc((-27,48),(-32,42)).segment((-32,33)).arc((-46,0),(-32,-33)).close().assemble().finalize().extrude(-131))