import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-100,0))
r=w0.sketch().circle(24).reset().face(w0.sketch().segment((-9,-20),(10,-20)).segment((10,20)).segment((-9,20)).segment((-9,2)).arc((-10,0),(-9,-2)).close().assemble(),mode='s').finalize().extrude(200)