import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,7,0))
r=w0.sketch().push([(47.5,50.5)]).rect(47,99).reset().face(w0.sketch().segment((28,73),(54,73)).segment((54,77)).arc((51,85),(51,93)).segment((38,96)).segment((37,93)).segment((38,93)).segment((38,83)).segment((28,83)).close().assemble(),mode='s').finalize().extrude(-55).union(w0.workplane(offset=40/2).moveTo(-57,-55).box(28,90,40))