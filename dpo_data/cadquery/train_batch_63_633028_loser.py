import cadquery as cq
w0=cq.Workplane('YZ',origin=(-21,0,0))
w1=cq.Workplane('YZ',origin=(-29,0,0))
r=w0.workplane(offset=-49/2).moveTo(-1,-32).cylinder(49,20).union(w0.sketch().segment((-100,-6),(-98,-8)).arc((-72,-12),(-50,-32)).segment((-19,-63)).segment((34,-9)).segment((-24,60)).close().assemble().finalize().extrude(91)).union(w1.sketch().segment((50,-12),(83,-12)).segment((83,-5)).arc((100,26),(83,55)).segment((83,63)).segment((50,63)).segment((50,55)).arc((33,26),(50,-5)).close().assemble().finalize().extrude(85))