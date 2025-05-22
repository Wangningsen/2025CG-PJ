import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-100,0))
r=w0.sketch().circle(40).reset().face(w0.sketch().segment((-13,37),(-12,21)).segment((-3,21)).segment((-4,37)).close().assemble(),mode='s').finalize().extrude(200)