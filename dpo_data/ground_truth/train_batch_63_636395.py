import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-100))
r=w0.workplane(offset=8/2).box(68,152,8).union(w0.sketch().segment((-26,-32),(26,-32)).segment((26,4)).segment((-26,-28)).close().assemble().finalize().extrude(200))