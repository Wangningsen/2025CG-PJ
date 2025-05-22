import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-50))
r=w0.sketch().arc((-14,55),(-59,-41),(46,-58)).segment((31,-58)).segment((31,-30)).segment((63,-30)).arc((66,-13),(65,3)).arc((67,91),(-14,55)).assemble().finalize().extrude(-44).union(w0.workplane(offset=144/2).moveTo(0,-10).cylinder(144,90))