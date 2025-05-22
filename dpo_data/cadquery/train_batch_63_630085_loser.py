import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-6))
r=w0.sketch().segment((-81,-29),(-38,-29)).arc((23,-91),(-11,-12)).segment((-11,2)).segment((-81,2)).close().assemble().finalize().extrude(-82).union(w0.workplane(offset=-5/2).moveTo(-16,85).cylinder(5,15)).union(w0.sketch().push([(33,8)]).rect(26,96).circle(6,mode='s').push([(77,-19)]).rect(8,100).finalize().extrude(94))