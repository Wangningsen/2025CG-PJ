import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-11))
w1=cq.Workplane('XY',origin=(0,0,-3))
r=w0.sketch().segment((-35,-81),(100,-81)).segment((100,61)).segment((9,61)).arc((-96,40),(-35,-45)).close().assemble().push([(33,-10)]).circle(43,mode='s').finalize().extrude(58).union(w1.workplane(offset=-44/2).moveTo(-30,23).box(4,2,44))