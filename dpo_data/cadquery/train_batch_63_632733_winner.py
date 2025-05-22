import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-50))
r=w0.sketch().arc((-24,50),(-59,-40),(31,-67)).segment((31,-30)).segment((63,-30)).arc((66,-14),(65,3)).arc((66,92),(-14,50)).close().assemble().finalize().extrude(-44).union(w0.workplane(offset=144/2).moveTo(0,-10).cylinder(144,90))