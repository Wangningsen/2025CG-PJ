import cadquery as cq
w0=cq.Workplane('YZ',origin=(-52,0,0))
r=w0.sketch().segment((-100,7),(-97,3)).segment((-90,3)).segment((-90,-7)).segment((-48,-65)).segment((-51,-68)).arc((-29,-72),(-7,-69)).arc((100,-7),(3,70)).arc((-65,65),(-100,7)).assemble().finalize().extrude(-13).union(w0.workplane(offset=118/2).moveTo(-26,2).cylinder(118,28))