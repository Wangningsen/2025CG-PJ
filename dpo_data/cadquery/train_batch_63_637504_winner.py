import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,42))
w1=cq.Workplane('XY',origin=(0,0,13))
r=w0.sketch().segment((-100,27),(-87,-12)).segment((0,17)).segment((-13,57)).close().assemble().push([(32.5,18)]).rect(13,14).push([(79,-39)]).circle(21).finalize().extrude(-84).union(w1.sketch().arc((54,53),(-7,0),(70,7)).segment((92,7)).segment((92,28)).arc((71,33),(54,53)).assemble().finalize().extrude(-13))