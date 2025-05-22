import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-6,0))
r=w0.sketch().push([(53,-39.5)]).rect(94,9).push([(53,-40)]).circle(2,mode='s').finalize().extrude(-16).union(w0.sketch().push([(-85,29)]).circle(15).circle(13,mode='s').finalize().extrude(28))