import cadquery as cq
w0=cq.Workplane('YZ',origin=(-28,0,0))
w1=cq.Workplane('YZ',origin=(-27,0,0))
r=w0.workplane(offset=-35/2).moveTo(5,24).cylinder(35,3).union(w0.sketch().arc((-7,46),(-5,-100),(18,44)).segment((18,100)).segment((-7,100)).close().assemble().finalize().extrude(91)).union(w1.workplane(offset=80/2).moveTo(5,24).cylinder(80,6))