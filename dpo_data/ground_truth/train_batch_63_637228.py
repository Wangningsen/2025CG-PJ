import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-58,0))
w1=cq.Workplane('ZX',origin=(0,-77,0))
r=w0.sketch().segment((-62,-86),(-31,-86)).segment((-31,-19)).arc((47,-2),(29,75)).segment((29,36)).segment((-52,36)).segment((-52,47)).arc((-56,27),(-52,7)).segment((-62,7)).close().assemble().finalize().extrude(144).union(w0.workplane(offset=149/2).moveTo(42.5,-37.5).box(21,115,149)).union(w1.sketch().segment((-100,-41),(100,-41)).segment((100,95)).segment((-35,95)).arc((-57,86),(-80,95)).segment((-100,95)).close().assemble().push([(-57,43)]).circle(33,mode='s').finalize().extrude(-13))