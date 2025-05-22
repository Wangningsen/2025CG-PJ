import cadquery as cq
w0=cq.Workplane('YZ',origin=(39,0,0))
r=w0.workplane(offset=-94/2).moveTo(0,31).cylinder(94,66).union(w0.sketch().segment((-69,-100),(5,-100)).segment((5,-38)).arc((65,7),(48,81)).arc((40,84),(35,90)).arc((-27,94),(-67,46)).segment((-69,46)).close().assemble().finalize().extrude(17))