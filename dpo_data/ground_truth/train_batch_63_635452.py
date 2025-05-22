import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,15))
r=w0.workplane(offset=-115/2).moveTo(0,-16).box(104,86,115).union(w0.sketch().segment((21,57),(21,59)).segment((22,59)).segment((23,57)).close().assemble().finalize().extrude(-4)).union(w0.workplane(offset=85/2).moveTo(0,-15).cylinder(85,10))