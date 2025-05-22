import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-83))
w1=cq.Workplane('ZX',origin=(0,-43,0))
r=w0.sketch().push([(-44,0)]).circle(56).reset().face(w0.sketch().segment((-65,48),(-39,7)).segment((-23,17)).segment((-49,58)).close().assemble(),mode='s').finalize().extrude(165).union(w1.workplane(offset=88/2).moveTo(-41,51).box(18,98,88))