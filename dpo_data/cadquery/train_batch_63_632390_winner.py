import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-46,0))
w1=cq.Workplane('ZX',origin=(0,-56,0))
r=w0.sketch().push([(61,0)]).circle(39).push([(60.5,0)]).rect(15,62,mode='s').finalize().extrude(101).union(w1.workplane(offset=81/2).moveTo(-98,-17).cylinder(81,2))