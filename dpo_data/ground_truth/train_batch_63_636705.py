import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-15,0))
r=w0.sketch().push([(-21.5,-70)]).rect(77,60).push([(47,86.5)]).rect(26,27).finalize().extrude(-46).union(w0.workplane(offset=77/2).moveTo(-24,30).cylinder(77,9))