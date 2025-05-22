import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,7,0))
r=w0.sketch().arc((-32,-1),(21,-58),(28,21)).arc((-20,58),(-32,-1)).assemble().finalize().extrude(-107).union(w0.sketch().segment((-51,-43),(42,-43)).segment((42,-13)).segment((19,-13)).arc((12,-2),(4,-13)).segment((-51,-13)).close().assemble().finalize().extrude(93))