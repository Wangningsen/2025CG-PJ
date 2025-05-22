import cadquery as cq
w0=cq.Workplane('YZ',origin=(1,0,0))
r=w0.workplane(offset=-40/2).moveTo(-10,91).cylinder(40,9).union(w0.workplane(offset=-40/2).moveTo(-21.5,-94.5).box(13,11,40)).union(w0.sketch().segment((-18,-5),(-4,-5)).arc((28,0),(-3,10)).segment((-3,58)).segment((-18,58)).close().assemble().finalize().extrude(37))