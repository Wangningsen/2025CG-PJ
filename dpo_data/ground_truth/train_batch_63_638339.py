import cadquery as cq
w0=cq.Workplane('YZ',origin=(-92,0,0))
r=w0.workplane(offset=91/2).cylinder(91,100).union(w0.sketch().segment((-68,-11),(68,-11)).segment((68,11)).segment((-38,11)).arc((-42,9),(-47,11)).segment((-68,11)).close().assemble().finalize().extrude(184))