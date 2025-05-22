import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-82,0))
r=w0.sketch().segment((-92,-84),(7,-100)).segment((16,-47)).arc((86,55),(-42,67)).segment((-67,67)).close().assemble().reset().face(w0.sketch().segment((-50,-13),(-43,-17)).arc((-44,-11),(-46,-4)).close().assemble(),mode='s').finalize().extrude(164)