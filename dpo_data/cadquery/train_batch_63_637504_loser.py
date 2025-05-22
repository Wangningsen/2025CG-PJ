import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-42))
w1=cq.Workplane('XY',origin=(0,0,12))
r=w0.sketch().segment((-100,27),(-87,-12)).segment((0,17)).segment((-13,57)).close().assemble().push([(32.5,18)]).rect(13,14).push([(33,18)]).circle(4,mode='s').push([(79,-39)]).circle(21).finalize().extrude(84).union(w1.sketch().segment((-5,2),(4,2)).arc((42,-25),(79,2)).segment((92,2)).segment((92,27)).segment((79,27)).arc((42,59),(4,27)).segment((-5,27)).close().assemble().finalize().extrude(-12))