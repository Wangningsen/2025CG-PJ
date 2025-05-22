import cadquery as cq
w0=cq.Workplane('YZ',origin=(-40,0,0))
r=w0.sketch().segment((-67,68),(-64,40)).arc((54,-40),(-39,69)).segment((-40,62)).close().assemble().finalize().extrude(-60).union(w0.workplane(offset=140/2).moveTo(-26,-70).cylinder(140,11))