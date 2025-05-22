import cadquery as cq
w0=cq.Workplane('YZ',origin=(-30,0,0))
w1=cq.Workplane('ZX',origin=(0,50,0))
r=w0.sketch().segment((19,42),(30,42)).arc((25,43),(19,42)).assemble().finalize().extrude(55).union(w1.sketch().segment((-39,-100),(90,-100)).segment((90,4)).segment((21,4)).arc((-53,95),(-39,-21)).close().assemble().finalize().extrude(-100))