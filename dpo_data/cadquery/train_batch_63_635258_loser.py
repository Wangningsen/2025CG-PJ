import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-4,0))
r=w0.workplane(offset=-56/2).moveTo(71,8).cylinder(56,29).union(w0.sketch().segment((-100,15),(-54,-12)).arc((-41,-53),(2,-58)).arc((93,-51),(17,0)).segment((-30,16)).segment((-6,57)).segment((-57,88)).close().assemble().reset().face(w0.sketch().segment((25,71),(56,70)).arc((40,76),(25,71)).assemble()).finalize().extrude(64))