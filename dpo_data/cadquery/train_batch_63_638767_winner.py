import cadquery as cq
w0=cq.Workplane('YZ',origin=(-75,0,0))
r=w0.sketch().segment((-92,-45),(22,-100)).segment((92,45)).segment((-22,100)).close().assemble().finalize().extrude(95).union(w0.workplane(offset=151/2).box(18,46,151))