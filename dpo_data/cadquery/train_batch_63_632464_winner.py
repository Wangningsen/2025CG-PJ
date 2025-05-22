import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,18))
r=w0.sketch().segment((-75,-11),(-46,-31)).segment((-31,-11)).close().assemble().finalize().extrude(-36).union(w0.sketch().push([(47,24)]).circle(53).circle(18,mode='s').finalize().extrude(-11)).union(w0.sketch().push([(-38.5,-21)]).rect(123,112).push([(-19,-27)]).circle(28,mode='s').finalize().extrude(-4))