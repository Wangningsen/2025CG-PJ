import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-100,0))
r=w0.sketch().segment((-25,-16),(25,-16)).segment((25,-7)).arc((0,-9),(-25,-7)).close().assemble().finalize().extrude(168).union(w0.workplane(offset=200/2).box(82,74,200))