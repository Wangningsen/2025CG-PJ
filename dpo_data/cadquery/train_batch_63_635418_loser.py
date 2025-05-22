import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,5))
r=w0.sketch().push([(-33,44)]).rect(28,36).push([(-16,31)]).circle(2).push([(30,-43.5)]).rect(36,37).finalize().extrude(-105).union(w0.sketch().push([(-19,31)]).circle(29).push([(-19,30.5)]).rect(36,3,mode='s').finalize().extrude(95))