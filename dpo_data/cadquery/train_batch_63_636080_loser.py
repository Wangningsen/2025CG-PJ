import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-38,0))
r=w0.sketch().push([(-36.5,-23)]).rect(39,32).push([(-36.5,-80.5)]).rect(39,33).push([(39,-26)]).circle(26).push([(49,67)]).rect(42,66).circle(14,mode='s').finalize().extrude(38).union(w0.workplane(offset=76/2).moveTo(-48,-77).box(44,46,76))