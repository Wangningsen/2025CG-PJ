import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-82,0))
r=w0.sketch().segment((-92,-84),(7,-100)).segment((17,-46)).arc((83,61),(-44,64)).segment((-66,67)).close().assemble().reset().face(w0.sketch().arc((-48,-1),(-46,-11),(-43,-19)).arc((-45,-10),(-48,-1)).assemble(),mode='s').finalize().extrude(164)