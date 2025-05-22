import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,0,0))
r=w0.sketch().push([(-36.5,-52)]).rect(39,90).push([(-36.5,-51.5)]).rect(39,25,mode='s').push([(39,-26)]).circle(26).push([(49,67)]).rect(42,66).circle(14,mode='s').finalize().extrude(-37).union(w0.workplane(offset=38/2).moveTo(-48,-77).box(44,46,38))