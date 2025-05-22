import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,34))
w1=cq.Workplane('ZX',origin=(0,5,0))
r=w0.workplane(offset=-97/2).moveTo(-86,13).cylinder(97,14).union(w0.sketch().push([(36,2)]).circle(64).push([(36,2)]).rect(122,22,mode='s').finalize().extrude(-77)).union(w0.workplane(offset=-19/2).moveTo(36,2).cylinder(19,21)).union(w1.sketch().push([(48,36)]).circle(15).push([(36,35)]).circle(1,mode='s').finalize().extrude(-65))