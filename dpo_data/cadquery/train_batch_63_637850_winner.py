import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,35,0))
r=w0.sketch().push([(-27,0)]).circle(53).push([(70,-4.5)]).rect(60,119).rect(24,53,mode='s').finalize().extrude(-70).union(w0.workplane(offset=-45/2).moveTo(-27,0).cylinder(45,73))