import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-22))
r=w0.sketch().segment((-100,27),(-2,27)).segment((-2,-63)).arc((2,-48),(3,-31)).segment((100,-31)).segment((100,63)).segment((-32,63)).segment((-32,28)).arc((-66,35),(-100,27)).assemble().finalize().extrude(45)