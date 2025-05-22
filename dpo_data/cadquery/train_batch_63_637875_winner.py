import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-100,0))
r=w0.sketch().circle(15).reset().face(w0.sketch().segment((-3,-10),(12,-10)).segment((11,13)).segment((-3,13)).segment((-3,10)).arc((-7,3),(-3,-5)).close().assemble(),mode='s').finalize().extrude(200)