import cadquery as cq
w0=cq.Workplane('YZ',origin=(24,0,0))
r=w0.sketch().segment((24,37),(34,37)).segment((28,14)).segment((66,4)).segment((74,35)).segment((91,35)).segment((92,67)).segment((82,68)).segment((88,90)).segment((50,100)).segment((42,69)).segment((25,70)).close().assemble().finalize().extrude(-54).union(w0.workplane(offset=6/2).moveTo(-51.5,-95).box(81,10,6))