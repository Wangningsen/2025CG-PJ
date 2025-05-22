import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,17))
r=w0.sketch().segment((-74,-11),(-45,-31)).segment((-31,-11)).close().assemble().finalize().extrude(-35).union(w0.sketch().push([(47,24)]).circle(53).circle(18,mode='s').finalize().extrude(-10)).union(w0.sketch().push([(-38.5,-21)]).rect(123,112).push([(-20,-27)]).circle(28,mode='s').finalize().extrude(-4))