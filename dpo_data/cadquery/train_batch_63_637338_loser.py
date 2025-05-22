import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-25))
r=w0.sketch().arc((-66,31),(-82,-57),(-2,-33)).segment((-2,-88)).segment((100,-88)).segment((100,68)).segment((3,68)).arc((-52,83),(-66,31)).assemble().reset().face(w0.sketch().arc((-2,-5),(-1,9),(-2,24)).close().assemble(),mode='s').finalize().extrude(50)