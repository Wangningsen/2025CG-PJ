import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,96))
r=w0.sketch().segment((-100,10),(-58,10)).arc((91,-36),(-33,58)).segment((-100,58)).close().assemble().reset().face(w0.sketch().arc((-44,46),(-42,49),(-40,51)).arc((-49,54),(-44,46)).assemble(),mode='s').finalize().extrude(-191)