import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,29))
r=w0.sketch().segment((-85,-3),(-85,10)).arc((-86,-35),(-52,-3)).close().assemble().reset().face(w0.sketch().segment((76,14),(87,10)).segment((100,38)).segment((98,38)).close().assemble()).finalize().extrude(-78).union(w0.workplane(offset=20/2).moveTo(84,-9).cylinder(20,8))