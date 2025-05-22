import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,26))
r=w0.sketch().segment((-100,61),(-98,54)).segment((-90,56)).segment((-92,64)).close().assemble().reset().face(w0.sketch().segment((-39,-53),(-1,-57)).segment((-1,-26)).segment((34,-25)).arc((98,-43),(40,-11)).segment((40,-10)).segment((-32,-1)).close().assemble()).finalize().extrude(-53)