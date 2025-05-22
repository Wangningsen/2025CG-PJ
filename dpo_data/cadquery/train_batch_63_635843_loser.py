import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-34,0))
r=w0.sketch().arc((-20,-55),(-54,-85),(-8,-85)).segment((56,-84)).segment((55,11)).segment((-20,10)).close().assemble().finalize().extrude(30).union(w0.sketch().segment((-47,-30),(36,-30)).arc((34,-27),(32,-23)).segment((33,-23)).segment((33,11)).arc((35,87),(-42,73)).segment((-47,73)).close().assemble().finalize().extrude(67))