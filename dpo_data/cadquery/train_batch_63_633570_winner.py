import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-52))
r=w0.sketch().push([(84,42)]).circle(16).push([(89,30)]).circle(2,mode='s').finalize().extrude(-23).union(w0.sketch().segment((-100,-58),(-56,-58)).arc((-62,-45),(-56,-32)).segment((-100,-32)).close().assemble().finalize().extrude(127))