import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,97,0))
r=w0.sketch().push([(61,-2)]).circle(39).push([(60,8)]).rect(4,16,mode='s').finalize().extrude(-194).union(w0.workplane(offset=-160/2).moveTo(-82,23).cylinder(160,18))