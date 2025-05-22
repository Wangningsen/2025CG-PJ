import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-2))
r=w0.sketch().arc((-72,21),(-53,-83),(-1,6)).arc((-42,-25),(-59,20)).arc((-66,20),(-72,21)).assemble().reset().face(w0.sketch().segment((48,-51),(51,-54)).segment((100,38)).segment((97,39)).close().assemble()).finalize().extrude(-4).union(w0.workplane(offset=7/2).moveTo(36,58).cylinder(7,26))