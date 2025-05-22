import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,69))
r=w0.sketch().segment((-100,5),(-45,-45)).segment((-15,-12)).segment((-70,38)).close().assemble().push([(-57,-3)]).circle(7,mode='s').finalize().extrude(-139).union(w0.sketch().segment((-39,-72),(100,-72)).segment((100,72)).segment((-39,72)).segment((-39,23)).arc((-90,-3),(-39,-30)).close().assemble().finalize().extrude(-71))