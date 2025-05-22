import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,85,0))
r=w0.workplane(offset=-169/2).moveTo(38.5,-55).box(51,72,169).union(w0.sketch().push([(39,-55)]).circle(45).push([(19,70)]).rect(84,60).finalize().extrude(-110)).union(w0.workplane(offset=-79/2).moveTo(-24,-19).cylinder(79,59))