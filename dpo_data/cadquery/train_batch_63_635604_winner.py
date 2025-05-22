import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,14,0))
r=w0.sketch().push([(38.5,-1)]).rect(123,122).push([(77,-1)]).circle(4,mode='s').finalize().extrude(-105).union(w0.sketch().push([(-50.5,17)]).rect(99,90).push([(-51,17)]).circle(7,mode='s').finalize().extrude(77))