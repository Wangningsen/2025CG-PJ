import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,80))
r=w0.sketch().segment((-58,-100),(58,-100)).segment((58,-30)).arc((67,-1),(58,30)).segment((58,100)).segment((-58,100)).segment((-58,30)).arc((-67,-1),(-58,-30)).close().assemble().push([(-1,-1)]).circle(26,mode='s').finalize().extrude(-160)