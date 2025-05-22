import cadquery as cq
w0=cq.Workplane('YZ',origin=(-34,0,0))
w1=cq.Workplane('YZ',origin=(-64,0,0))
r=w0.sketch().segment((80,68),(80,70)).segment((84,70)).segment((84,66)).segment((82,66)).arc((98,79),(80,68)).assemble().finalize().extrude(-30).union(w0.workplane(offset=98/2).moveTo(69.5,-5.5).box(61,15,98)).union(w1.workplane(offset=30/2).moveTo(-43.5,-39.5).box(113,93,30))