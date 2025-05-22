import cadquery as cq
w0=cq.Workplane('YZ',origin=(61,0,0))
r=w0.sketch().arc((-23,8),(-85,-79),(8,-28)).segment((100,-28)).segment((100,96)).segment((-23,96)).close().assemble().reset().face(w0.sketch().segment((-23,11),(34,-25)).segment((94,54)).segment((46,90)).close().assemble(),mode='s').finalize().extrude(-122)