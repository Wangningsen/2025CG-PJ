import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-82,0))
r=w0.sketch().segment((-92,-84),(7,-100)).segment((16,-46)).arc((83,62),(-45,64)).segment((-67,68)).close().assemble().reset().face(w0.sketch().segment((-50,-2),(-45,-17)).segment((-43,-17)).segment((-47,-1)).close().assemble(),mode='s').finalize().extrude(165)