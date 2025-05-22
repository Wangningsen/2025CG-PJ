import cadquery as cq
w0=cq.Workplane('YZ',origin=(-1,0,0))
r=w0.workplane(offset=-91/2).cylinder(91,100).union(w0.sketch().segment((-68,-11),(68,-11)).segment((68,11)).segment((-43,11)).arc((-46,9),(-50,11)).segment((-68,11)).close().assemble().finalize().extrude(93))