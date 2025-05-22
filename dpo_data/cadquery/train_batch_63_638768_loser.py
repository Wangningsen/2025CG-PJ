import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,36))
w1=cq.Workplane('ZX',origin=(0,-15,0))
r=w0.sketch().push([(6,19)]).circle(44).circle(26,mode='s').finalize().extrude(-45).union(w0.sketch().segment((-32,37),(-19,7)).segment((61,39)).segment((48,69)).close().assemble().push([(10.5,24.5)]).rect(13,5,mode='s').push([(24,29)]).circle(4,mode='s').push([(43,86)]).circle(14).finalize().extrude(-18)).union(w1.workplane(offset=-85/2).moveTo(-3,-31).box(66,60,85))