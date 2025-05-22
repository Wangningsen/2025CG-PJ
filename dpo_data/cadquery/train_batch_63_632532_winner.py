import cadquery as cq
w0=cq.Workplane('YZ',origin=(-18,0,0))
w1=cq.Workplane('YZ',origin=(6,0,0))
r=w0.workplane(offset=35/2).moveTo(-53,-21).cylinder(35,47).union(w1.sketch().segment((12,54),(32,54)).arc((22,31),(34,8)).arc((74,-46),(74,22)).arc((76,37),(70,51)).segment((70,57)).segment((63,57)).arc((46,68),(29,57)).segment((12,57)).close().assemble().finalize().extrude(-24))