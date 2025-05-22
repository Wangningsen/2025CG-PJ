import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-25))
r=w0.sketch().segment((-71,-98),(-68,-100)).segment((-44,-71)).segment((-46,-69)).close().assemble().reset().face(w0.sketch().segment((-47,-5),(-34,-5)).arc((71,4),(-34,11)).segment((-43,11)).segment((-43,100)).segment((-47,100)).close().assemble()).finalize().extrude(51)