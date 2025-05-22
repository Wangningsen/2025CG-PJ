import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,6,0))
r=w0.sketch().push([(47.5,50.5)]).rect(47,99).reset().face(w0.sketch().segment((25,73),(54,73)).segment((54,83)).segment((48,83)).arc((45,96),(41,83)).segment((25,83)).close().assemble(),mode='s').finalize().extrude(-54).union(w0.workplane(offset=41/2).moveTo(-57,-55).box(28,90,41))