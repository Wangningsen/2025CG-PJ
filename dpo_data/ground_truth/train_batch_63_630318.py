import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,50,0))
r=w0.sketch().segment((-39,-100),(90,-100)).segment((90,4)).segment((21,4)).arc((-52,95),(-39,-21)).close().assemble().finalize().extrude(-99).union(w0.workplane(offset=-18/2).moveTo(37,5.5).box(16,37,18))