import cadquery as cq
w0=cq.Workplane('YZ',origin=(-30,0,0))
w1=cq.Workplane('YZ',origin=(-36,0,0))
r=w0.sketch().segment((1,-69),(2,-69)).arc((39,-100),(76,-69)).segment((78,-69)).segment((78,-50)).segment((76,-50)).arc((39,-20),(2,-50)).segment((1,-50)).close().assemble().finalize().extrude(-6).union(w0.sketch().arc((-79,54),(-55,33),(-71,5)).segment((13,5)).segment((13,100)).segment((-79,100)).close().assemble().finalize().extrude(66)).union(w1.workplane(offset=39/2).moveTo(39,-59).cylinder(39,31))