import cadquery as cq
w0=cq.Workplane('YZ',origin=(-84,0,0))
r=w0.sketch().segment((35,-100),(63,-100)).segment((63,3)).segment((35,3)).segment((35,-28)).segment((37,-28)).segment((37,-31)).segment((35,-31)).close().assemble().finalize().extrude(158).union(w0.workplane(offset=168/2).moveTo(-15,52).cylinder(168,48))