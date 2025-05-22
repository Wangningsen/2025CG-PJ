import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-21,0))
r=w0.sketch().segment((-42,-100),(42,-100)).segment((42,-20)).arc((-1,27),(3,91)).arc((-21,91),(-42,100)).close().assemble().finalize().extrude(41)