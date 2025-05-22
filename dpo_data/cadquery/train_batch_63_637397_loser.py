import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,39,0))
w1=cq.Workplane('ZX',origin=(0,55,0))
r=w0.workplane(offset=47/2).moveTo(59.5,-12).box(81,116,47).union(w1.sketch().push([(-44,30)]).rect(112,80).rect(112,18,mode='s').finalize().extrude(-141))