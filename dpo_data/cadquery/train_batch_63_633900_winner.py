import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,96))
r=w0.sketch().segment((-100,10),(-58,10)).arc((92,-35),(-32,59)).segment((-100,58)).close().assemble().reset().face(w0.sketch().segment((-51,49),(-43,46)).segment((-40,54)).segment((-48,58)).close().assemble(),mode='s').finalize().extrude(-192)