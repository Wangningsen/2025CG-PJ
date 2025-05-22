import cadquery as cq
w0=cq.Workplane('YZ',origin=(-12,0,0))
w1=cq.Workplane('ZX',origin=(0,-100,0))
r=w0.sketch().segment((-27,-4),(-22,-4)).arc((-25,0),(-27,4)).close().assemble().finalize().extrude(8).union(w1.workplane(offset=200/2).box(138,24,200))