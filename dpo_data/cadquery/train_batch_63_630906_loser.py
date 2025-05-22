import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,38,0))
r=w0.workplane(offset=-113/2).moveTo(26,26).box(148,142,113).union(w0.sketch().push([(-80,-76)]).circle(20).push([(25.5,26)]).rect(85,24).finalize().extrude(37))