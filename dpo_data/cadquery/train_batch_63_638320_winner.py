import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,1,0))
r=w0.workplane(offset=-31/2).moveTo(0,46).cylinder(31,54).union(w0.sketch().push([(17,-70.5)]).rect(60,59).push([(17,-71)]).circle(12,mode='s').finalize().extrude(29))