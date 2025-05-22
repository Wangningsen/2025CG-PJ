import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,70,0))
w1=cq.Workplane('YZ',origin=(-95,0,0))
r=w0.sketch().segment((-100,93),(-97,93)).segment((-98,95)).close().assemble().reset().face(w0.sketch().segment((-78,-84),(-76,-85)).segment((-75,-84)).close().assemble()).reset().face(w0.sketch().segment((-27,-18),(2,21)).segment((-27,42)).close().assemble()).finalize().extrude(-140).union(w1.sketch().arc((3,87),(11,95),(19,100)).segment((3,100)).close().assemble().finalize().extrude(143))