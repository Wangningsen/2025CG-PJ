import cadquery as cq
w0=cq.Workplane('YZ',origin=(43,0,0))
r=w0.sketch().segment((-100,-13),(-16,-73)).segment((10,-38)).segment((10,-39)).arc((100,12),(4,59)).segment((34,59)).segment((34,13)).segment((-14,13)).segment((-14,32)).arc((-18,7),(-12,-19)).segment((-72,25)).close().assemble().finalize().extrude(-118).union(w0.workplane(offset=32/2).moveTo(-42,32).cylinder(32,42))