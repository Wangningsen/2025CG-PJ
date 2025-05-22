import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,33))
w1=cq.Workplane('XY',origin=(0,0,47))
r=w0.sketch().segment((-99,-14),(-74,-15)).segment((-70,68)).segment((-95,69)).close().assemble().reset().face(w0.sketch().segment((5,-12),(99,-12)).segment((99,84)).segment((77,84)).arc((53,100),(28,84)).segment((5,84)).close().assemble()).finalize().extrude(-80).union(w1.sketch().segment((-77,-100),(13,-100)).segment((13,-92)).arc((58,-44),(13,5)).segment((13,62)).segment((-77,62)).close().assemble().push([(-32,-19)]).circle(13,mode='s').finalize().extrude(-10))