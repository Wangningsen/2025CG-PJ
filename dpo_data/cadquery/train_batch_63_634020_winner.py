import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-73,0))
r=w0.sketch().push([(0,-54.5)]).rect(104,91).push([(-8,80)]).circle(20).finalize().extrude(81).union(w0.workplane(offset=147/2).moveTo(-27,36).cylinder(147,11))