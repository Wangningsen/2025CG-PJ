import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-25))
r=w0.sketch().arc((-69,28),(-85,-55),(-2,-32)).segment((-2,-88)).segment((100,-88)).segment((100,68)).segment((4,68)).arc((-52,83),(-69,28)).assemble().reset().face(w0.sketch().arc((-11,13),(-6,4),(-2,-5)).segment((-2,20)).arc((-6,16),(-11,13)).assemble(),mode='s').finalize().extrude(50)