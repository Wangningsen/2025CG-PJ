import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-82))
w1=cq.Workplane('ZX',origin=(0,-43,0))
r=w0.sketch().push([(-44,0)]).circle(56).reset().face(w0.sketch().segment((-62,47),(-41,7)).segment((-23,17)).segment((-45,57)).close().assemble(),mode='s').finalize().extrude(165).union(w1.workplane(offset=88/2).moveTo(-41,53.5).box(18,93,88))