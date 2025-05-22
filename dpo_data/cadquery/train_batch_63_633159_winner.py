import cadquery as cq
w0=cq.Workplane('YZ',origin=(28,0,0))
r=w0.sketch().segment((-49,64),(-44,50)).segment((-36,54)).arc((-43,58),(-48,64)).close().assemble().finalize().extrude(-128).union(w0.workplane(offset=72/2).moveTo(0,-12).cylinder(72,52))