import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,2,0))
r=w0.sketch().arc((-15,37),(-83,-75),(36,-17)).arc((86,79),(-15,37)).assemble().finalize().extrude(-60).union(w0.workplane(offset=57/2).moveTo(-25.5,61).box(65,2,57))