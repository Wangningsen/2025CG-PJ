import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-49,0))
r=w0.sketch().circle(27).reset().face(w0.sketch().segment((10,-10),(13,-11)).segment((15,-3)).segment((12,-2)).close().assemble(),mode='s').finalize().extrude(-19).union(w0.workplane(offset=117/2).box(150,200,117))