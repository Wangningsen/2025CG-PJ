import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,7,0))
r=w0.sketch().push([(47.5,50.5)]).rect(47,99).push([(26,76.5)]).rect(2,1,mode='s').push([(39.5,84.5)]).rect(5,17,mode='s').push([(52.5,80)]).rect(3,14,mode='s').finalize().extrude(-55).union(w0.workplane(offset=40/2).moveTo(-57,-55).box(28,90,40))