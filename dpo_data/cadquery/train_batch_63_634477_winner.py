import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-12,0))
w1=cq.Workplane('ZX',origin=(0,-3,0))
r=w0.sketch().push([(-15,-86)]).circle(14).push([(-19,-85)]).circle(5,mode='s').finalize().extrude(-13).union(w1.sketch().push([(0,78.5)]).rect(66,43).push([(0,78)]).circle(13,mode='s').push([(7.5,93)]).rect(7,2,mode='s').finalize().extrude(28))