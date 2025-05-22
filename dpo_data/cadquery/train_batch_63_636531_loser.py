import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,49,0))
w1=cq.Workplane('ZX',origin=(0,13,0))
r=w0.workplane(offset=-98/2).moveTo(60,-34).cylinder(98,18).union(w0.sketch().push([(26,-64)]).rect(68,72).push([(26,-63)]).circle(23,mode='s').finalize().extrude(-36)).union(w1.sketch().push([(-40,62)]).circle(38).circle(22,mode='s').finalize().extrude(-42))