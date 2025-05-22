import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,84,0))
r=w0.workplane(offset=-169/2).moveTo(38.5,-55).box(51,72,169).union(w0.sketch().push([(19,70)]).rect(84,60).push([(38,-55)]).circle(45).finalize().extrude(-109)).union(w0.workplane(offset=-78/2).moveTo(-24,-18).cylinder(78,60))