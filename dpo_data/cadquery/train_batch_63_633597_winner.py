import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-38,0))
w1=cq.Workplane('ZX',origin=(0,-39,0))
r=w0.sketch().arc((15,83),(33,72),(40,53)).segment((59,73)).segment((33,100)).close().assemble().finalize().extrude(-12).union(w0.sketch().segment((-31,-30),(24,-30)).arc((-4,-6),(-31,-30)).assemble().finalize().extrude(89)).union(w1.workplane(offset=1/2).moveTo(-47.5,-78).box(23,44,1))