import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,27,0))
r=w0.sketch().circle(100).reset().face(w0.sketch().segment((-77,63),(-69,-8)).segment((14,2)).segment((7,73)).close().assemble(),mode='s').finalize().extrude(-54)