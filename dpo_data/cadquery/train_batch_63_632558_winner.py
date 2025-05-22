import cadquery as cq
w0=cq.Workplane('YZ',origin=(51,0,0))
r=w0.sketch().arc((-33,-5),(-86,-85),(-5,-33)).arc((80,78),(-33,-5)).assemble().finalize().extrude(-113).union(w0.workplane(offset=12/2).moveTo(64,70).cylinder(12,13))