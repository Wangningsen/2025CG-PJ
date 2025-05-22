import cadquery as cq
w0=cq.Workplane('YZ',origin=(-62,0,0))
r=w0.sketch().arc((-33,-5),(-86,-85),(-5,-33)).arc((78,80),(-33,-5)).assemble().finalize().extrude(112).union(w0.workplane(offset=125/2).moveTo(66,63).cylinder(125,11))