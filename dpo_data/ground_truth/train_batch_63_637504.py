import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-41))
w1=cq.Workplane('XY',origin=(0,0,1))
r=w0.sketch().segment((-100,27),(-87,-12)).segment((0,17)).segment((-13,57)).close().assemble().push([(32.5,18)]).rect(13,14).push([(79,-39)]).circle(21).finalize().extrude(83).union(w1.sketch().segment((-29,7),(-9,7)).arc((31,-24),(72,7)).segment((92,7)).segment((92,28)).segment((72,28)).arc((31,60),(-9,28)).segment((-29,28)).close().assemble().finalize().extrude(12))