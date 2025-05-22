import cadquery as cq
w0=cq.Workplane('YZ',origin=(43,0,0))
w1=cq.Workplane('ZX',origin=(0,-22,0))
r=w0.sketch().segment((-100,-32),(-85,-32)).arc((-41,-65),(4,-32)).segment((19,-32)).segment((19,-5)).segment((4,-5)).arc((-41,28),(-85,-5)).segment((-100,-5)).close().assemble().finalize().extrude(24).union(w1.sketch().arc((52,-67),(65,-47),(52,-26)).close().assemble().finalize().extrude(122))