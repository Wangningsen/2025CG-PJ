import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,13))
w1=cq.Workplane('YZ',origin=(-6,0,0))
r=w0.sketch().segment((-100,48),(-78,-78)).segment((-11,-67)).arc((12,-72),(35,-63)).segment((100,-48)).segment((78,78)).segment((11,67)).arc((-12,72),(-35,63)).close().assemble().finalize().extrude(-11).union(w1.workplane(offset=90/2).moveTo(0,-10).cylinder(90,3))