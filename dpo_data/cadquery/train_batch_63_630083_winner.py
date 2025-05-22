import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-13,0))
r=w0.sketch().push([(-32,-75)]).circle(25).push([(24,68)]).circle(6).finalize().extrude(-34).union(w0.workplane(offset=60/2).moveTo(24,68.5).box(66,63,60))