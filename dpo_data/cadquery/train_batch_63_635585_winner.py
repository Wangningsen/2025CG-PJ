import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,16,0))
r=w0.sketch().segment((99,-94),(100,-93)).segment((100,-85)).arc((99,-89),(99,-94)).assemble().finalize().extrude(-32).union(w0.sketch().segment((-100,76),(-76,-37)).segment((7,-19)).segment((-17,94)).close().assemble().finalize().extrude(-28))