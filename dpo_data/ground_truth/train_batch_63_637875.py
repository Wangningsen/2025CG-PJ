import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,100,0))
r=w0.sketch().segment((-3,-10),(12,-10)).arc((-14,-2),(9,13)).segment((-3,13)).segment((-3,10)).arc((-6,1),(-3,-5)).close().assemble().reset().face(w0.sketch().arc((12,-7),(15,1),(12,10)).segment((12,-5)).close().assemble()).finalize().extrude(-200)