import cadquery as cq
w0=cq.Workplane('YZ',origin=(-21,0,0))
w1=cq.Workplane('YZ',origin=(-21,0,0))
r=w0.sketch().arc((-52,9),(49,22),(-45,-34)).arc((97,21),(-52,9)).assemble().finalize().extrude(-23).union(w0.sketch().segment((-100,-55),(-78,-55)).arc((-48,-69),(-17,-55)).segment((4,-55)).segment((4,-26)).arc((11,-18),(16,-8)).segment((24,-8)).segment((24,50)).segment((18,50)).segment((18,48)).arc((-47,51),(-89,-1)).segment((-100,-1)).close().assemble().finalize().extrude(50)).union(w1.workplane(offset=66/2).moveTo(-48,15).cylinder(66,17))