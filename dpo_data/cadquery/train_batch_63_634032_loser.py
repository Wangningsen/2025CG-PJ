import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-43,0))
r=w0.sketch().push([(42,-41)]).rect(116,52).push([(1,-32)]).circle(4,mode='s').finalize().extrude(49).union(w0.workplane(offset=87/2).moveTo(-54,21).cylinder(87,46))