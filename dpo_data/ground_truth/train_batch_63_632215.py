import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-11))
r=w0.sketch().segment((-35,25),(-32,22)).segment((-32,21)).segment((-30,19)).arc((-32,23),(-35,25)).assemble().finalize().extrude(-36).union(w0.sketch().segment((-35,-81),(100,-81)).segment((100,61)).segment((9,61)).arc((-95,42),(-35,-45)).close().assemble().push([(33,-10)]).circle(43,mode='s').finalize().extrude(58))