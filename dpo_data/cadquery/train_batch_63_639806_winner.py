import cadquery as cq
w0=cq.Workplane('YZ',origin=(26,0,0))
r=w0.sketch().segment((13,-75),(100,-75)).segment((100,-18)).segment((75,-18)).arc((16,-1),(13,-61)).close().assemble().finalize().extrude(-51).union(w0.workplane(offset=-32/2).moveTo(-69.5,62).box(61,26,32))