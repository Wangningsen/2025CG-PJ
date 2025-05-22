import cadquery as cq
w0=cq.Workplane('YZ',origin=(21,0,0))
w1=cq.Workplane('YZ',origin=(21,0,0))
r=w0.sketch().segment((35,-12),(60,-12)).arc((68,-13),(77,-12)).segment((100,-12)).segment((100,68)).segment((94,68)).arc((26,90),(35,19)).close().assemble().push([(67,28.5)]).rect(20,29,mode='s').finalize().extrude(-41).union(w1.sketch().segment((-100,-97),(17,-99)).segment((18,-78)).segment((-100,-75)).close().assemble().finalize().extrude(-40))