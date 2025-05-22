import cadquery as cq
w0=cq.Workplane('YZ',origin=(34,0,0))
w1=cq.Workplane('ZX',origin=(0,24,0))
r=w0.sketch().segment((-100,18),(-87,18)).arc((-94,35),(-87,52)).segment((-100,52)).close().assemble().finalize().extrude(-22).union(w1.sketch().push([(-29,-11)]).circle(23).reset().face(w1.sketch().segment((-34,-23),(-27,-23)).segment((-27,-26)).segment((-25,-26)).segment((-25,-23)).segment((-17,-23)).segment((-17,-21)).segment((-25,-21)).segment((-25,-18)).segment((-27,-18)).segment((-27,-21)).segment((-34,-21)).close().assemble(),mode='s').finalize().extrude(76))