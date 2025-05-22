import cadquery as cq
w0=cq.Workplane('YZ',origin=(9,0,0))
w1=cq.Workplane('YZ',origin=(1,0,0))
r=w0.workplane(offset=-89/2).moveTo(52,39).cylinder(89,9).union(w0.workplane(offset=-28/2).moveTo(97,37).cylinder(28,3)).union(w1.sketch().push([(-60,-18.5)]).rect(80,59).reset().face(w1.sketch().arc((-52,1),(-69,-37),(-50,0)).segment((-45,0)).segment((-45,11)).segment((-52,11)).close().assemble(),mode='s').finalize().extrude(78))