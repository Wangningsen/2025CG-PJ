import cadquery as cq
w0=cq.Workplane('YZ',origin=(42,0,0))
r=w0.sketch().segment((-100,-13),(-15,-74)).segment((10,-40)).arc((100,17),(0,54)).segment((34,54)).segment((34,13)).segment((-14,13)).segment((-14,32)).arc((-18,5),(-9,-21)).segment((-72,25)).close().assemble().finalize().extrude(-118).union(w0.workplane(offset=33/2).moveTo(-42,32).cylinder(33,42))