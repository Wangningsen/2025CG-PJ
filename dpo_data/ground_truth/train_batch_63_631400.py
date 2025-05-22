import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,22,0))
r=w0.sketch().segment((6,0),(6,19)).arc((-100,10),(6,0)).assemble().finalize().extrude(-107).union(w0.sketch().segment((41,1),(47,-63)).segment((100,-58)).segment((94,6)).close().assemble().finalize().extrude(63))