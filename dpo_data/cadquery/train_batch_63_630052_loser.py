import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-35,0))
w1=cq.Workplane('YZ',origin=(80,0,0))
r=w0.sketch().segment((-100,-8),(-11,-8)).segment((-11,4)).arc((0,-17),(18,-30)).arc((35,-87),(63,-35)).arc((84,64),(-11,47)).segment((-11,87)).segment((-100,87)).close().assemble().finalize().extrude(112).union(w1.workplane(offset=-78/2).moveTo(-44.5,-56).box(67,18,78))