import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,52))
r=w0.workplane(offset=-131/2).moveTo(-92,0).cylinder(131,8).union(w0.sketch().arc((98,-30),(100,0),(98,30)).close().assemble().finalize().extrude(27))