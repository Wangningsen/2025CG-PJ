import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,86))
r=w0.sketch().segment((-100,-3),(-92,-3)).arc((0,-92),(92,-3)).segment((100,-3)).segment((100,3)).segment((92,3)).arc((0,92),(-92,3)).segment((-100,3)).close().assemble().circle(62,mode='s').finalize().extrude(-173)