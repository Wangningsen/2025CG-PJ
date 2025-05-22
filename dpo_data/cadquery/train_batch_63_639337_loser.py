import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-37,0))
r=w0.workplane(offset=58/2).moveTo(73,32).cylinder(58,27).union(w0.sketch().push([(-81.5,-27)]).rect(37,64).push([(28,-29.5)]).rect(116,17).finalize().extrude(74))