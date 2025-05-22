import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,13))
w1=cq.Workplane('YZ',origin=(-15,0,0))
r=w0.sketch().segment((-100,48),(-78,-78)).segment((-24,-69)).arc((12,-72),(46,-57)).segment((100,-48)).segment((78,78)).segment((24,69)).arc((-12,72),(-46,57)).close().assemble().finalize().extrude(-11).union(w1.workplane(offset=99/2).moveTo(0,-10).cylinder(99,3))