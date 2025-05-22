import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.sketch().rect(174,76).reset().face(w0.sketch().segment((-26,20),(-19,13)).arc((-16,-16),(13,-19)).segment((20,-25)).segment((26,-20)).segment((19,-13)).arc((16,16),(-13,19)).segment((-20,25)).close().assemble(),mode='s').finalize().extrude(-200)