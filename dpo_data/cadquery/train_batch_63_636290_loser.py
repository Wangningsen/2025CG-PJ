import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,20,0))
r=w0.sketch().segment((-42,-100),(42,-100)).segment((42,-23)).arc((-1,26),(3,91)).arc((-20,90),(-42,100)).close().assemble().finalize().extrude(-41)