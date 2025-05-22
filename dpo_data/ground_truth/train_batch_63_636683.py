import cadquery as cq
w0=cq.Workplane('YZ',origin=(55,0,0))
w1=cq.Workplane('YZ',origin=(55,0,0))
r=w0.workplane(offset=-78/2).moveTo(-52,16).cylinder(78,48).union(w1.sketch().arc((-3,-9),(96,-31),(11,23)).arc((-16,14),(-3,-9)).assemble().finalize().extrude(-109))