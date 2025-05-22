import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,65))
r=w0.sketch().segment((-68,-51),(-57,-59)).arc((-42,-83),(-14,-91)).segment((-7,-100)).segment((33,-50)).segment((24,-42)).arc((9,-19),(-19,-9)).segment((-28,-1)).close().assemble().push([(12,44)]).circle(56).finalize().extrude(-130)