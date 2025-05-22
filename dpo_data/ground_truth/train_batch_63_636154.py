import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,26))
r=w0.sketch().arc((-99,-100),(-68,-84),(-32,-83)).segment((-88,17)).segment((31,85)).segment((88,-17)).segment((-29,-83)).arc((-11,-90),(5,-100)).segment((99,-100)).segment((99,100)).segment((-99,100)).close().assemble().finalize().extrude(-53)