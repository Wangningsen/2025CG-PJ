import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,3,0))
r=w0.sketch().push([(-52.5,73.5)]).rect(75,3).push([(-52,73)]).circle(1,mode='s').push([(-28,49)]).circle(2).finalize().extrude(-103).union(w0.workplane(offset=97/2).moveTo(38,-29).box(104,92,97))