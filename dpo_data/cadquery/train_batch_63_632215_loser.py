import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-11))
r=w0.sketch().segment((-38,22),(-34,19)).segment((-30,22)).close().assemble().finalize().extrude(-36).union(w0.sketch().segment((-35,-81),(100,-81)).segment((100,61)).segment((9,61)).arc((-95,42),(-35,-45)).close().assemble().push([(32,-10)]).circle(43,mode='s').finalize().extrude(58))