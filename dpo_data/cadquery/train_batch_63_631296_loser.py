import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-23))
r=w0.sketch().segment((-100,27),(-2,27)).segment((-2,-63)).arc((1,-50),(3,-37)).segment((3,-31)).segment((100,-31)).segment((100,63)).segment((-32,63)).segment((-32,28)).arc((-66,35),(-100,27)).assemble().finalize().extrude(46)