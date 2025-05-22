import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-88,0))
r=w0.sketch().circle(100).reset().face(w0.sketch().segment((-40,-51),(-31,-51)).segment((-31,-68)).segment((31,-68)).segment((31,68)).segment((0,68)).segment((0,70)).segment((-40,70)).close().assemble(),mode='s').finalize().extrude(176)