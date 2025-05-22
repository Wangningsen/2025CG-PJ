import cadquery as cq
w0=cq.Workplane('YZ',origin=(-40,0,0))
r=w0.sketch().segment((-67,68),(-66,39)).arc((48,-45),(-41,67)).segment((-42,62)).close().assemble().finalize().extrude(-60).union(w0.workplane(offset=140/2).moveTo(-26,-70).cylinder(140,11))