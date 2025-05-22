import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-38,0))
r=w0.sketch().segment((15,83),(36,74)).segment((34,70)).arc((38,62),(40,54)).segment((59,73)).segment((33,100)).close().assemble().finalize().extrude(-12).union(w0.workplane(offset=-1/2).moveTo(-47.5,-78).box(23,44,1)).union(w0.sketch().segment((-31,-30),(24,-30)).arc((-3,-6),(-31,-30)).assemble().finalize().extrude(89))