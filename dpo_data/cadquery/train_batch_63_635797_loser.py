import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-47,0))
w1=cq.Workplane('YZ',origin=(23,0,0))
r=w0.workplane(offset=-18/2).moveTo(64,69).cylinder(18,21).union(w1.sketch().segment((-59,-83),(100,-83)).segment((100,56)).segment((-10,56)).arc((-94,27),(-59,-59)).close().assemble().finalize().extrude(-113))