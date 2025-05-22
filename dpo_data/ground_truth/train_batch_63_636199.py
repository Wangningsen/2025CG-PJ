import cadquery as cq
w0=cq.Workplane('YZ',origin=(82,0,0))
r=w0.sketch().segment((-100,-39),(-50,-39)).segment((-56,39)).segment((-100,39)).close().assemble().reset().face(w0.sketch().segment((-52,0),(-30,-43)).segment((52,0)).segment((30,43)).close().assemble()).reset().face(w0.sketch().segment((50,39),(56,-39)).segment((100,-39)).segment((100,39)).close().assemble()).finalize().extrude(-165)