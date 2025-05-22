import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-43,0))
r=w0.workplane(offset=73/2).moveTo(-48,-12).cylinder(73,52).union(w0.sketch().push([(44.5,45.5)]).rect(111,37).push([(86,-7)]).circle(3).finalize().extrude(87))