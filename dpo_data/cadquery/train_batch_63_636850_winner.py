import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-6,0))
r=w0.sketch().segment((-100,-4),(33,-4)).arc((82,-57),(54,11)).segment((54,62)).segment((-100,63)).close().assemble().reset().face(w0.sketch().segment((44,-10),(49,-54)).segment((84,-50)).segment((79,-7)).close().assemble(),mode='s').finalize().extrude(12)