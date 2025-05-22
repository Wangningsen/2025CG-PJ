import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,51,0))
r=w0.sketch().segment((-21,-6),(-4,-6)).segment((-4,-4)).segment((-2,-4)).segment((-2,-6)).segment((-3,-6)).arc((0,-7),(3,-6)).segment((21,-6)).segment((21,6)).segment((3,6)).arc((0,7),(-3,6)).segment((-21,6)).close().assemble().finalize().extrude(-151).union(w0.workplane(offset=49/2).box(102,170,49))