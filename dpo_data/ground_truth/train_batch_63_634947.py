import cadquery as cq
w0=cq.Workplane('YZ',origin=(70,0,0))
r=w0.workplane(offset=-140/2).cylinder(140,46).union(w0.sketch().segment((-32,-100),(32,-100)).segment((32,-31)).arc((45,0),(32,31)).segment((32,100)).segment((-32,100)).segment((-32,57)).arc((-27,50),(-32,42)).segment((-32,31)).arc((-45,0),(-32,-31)).close().assemble().finalize().extrude(-131))