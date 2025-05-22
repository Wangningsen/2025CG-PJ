import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,55,0))
w1=cq.Workplane('ZX',origin=(0,14,0))
r=w0.sketch().segment((-44,-70),(-11,-70)).segment((-11,0)).segment((19,0)).segment((19,50)).segment((-44,50)).close().assemble().finalize().extrude(-123).union(w0.sketch().segment((-63,-2),(-60,-5)).segment((-29,-85)).segment((73,-46)).segment((42,35)).segment((-39,4)).segment((-28,19)).arc((-27,37),(-9,44)).segment((26,91)).segment((13,100)).close().assemble().finalize().extrude(13)).union(w1.workplane(offset=15/2).moveTo(-36.5,-80.5).box(73,39,15))