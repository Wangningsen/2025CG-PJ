import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-100))
r=w0.sketch().circle(72).reset().face(w0.sketch().segment((-43,56),(-16,11)).arc((-16,-9),(4,-18)).segment((31,-63)).segment((43,-56)).segment((13,-11)).arc((16,11),(-4,18)).segment((-34,63)).close().assemble(),mode='s').finalize().extrude(200)