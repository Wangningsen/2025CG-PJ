import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,2,0))
r=w0.sketch().arc((-15,37),(-82,-76),(36,-17)).arc((84,80),(-15,37)).assemble().finalize().extrude(-60).union(w0.sketch().segment((-58,59),(-11,59)).segment((-11,61)).segment((-8,61)).segment((-8,59)).segment((6,59)).segment((6,62)).segment((-58,62)).close().assemble().finalize().extrude(57))