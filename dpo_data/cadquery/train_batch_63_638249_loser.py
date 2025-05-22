import cadquery as cq
w0=cq.Workplane('YZ',origin=(59,0,0))
r=w0.sketch().segment((-78,14),(75,14)).segment((75,100)).segment((-78,100)).segment((-78,83)).arc((-76,82),(-78,80)).close().assemble().finalize().extrude(-118).union(w0.workplane(offset=-75/2).moveTo(55.5,-94.5).box(45,11,75))