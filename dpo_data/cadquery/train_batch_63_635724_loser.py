import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,66,0))
w1=cq.Workplane('ZX',origin=(0,70,0))
r=w0.workplane(offset=-136/2).moveTo(23,0).box(154,128,136).union(w1.sketch().push([(-53,0)]).rect(94,166).push([(-80,-41)]).circle(12,mode='s').push([(-31,-40)]).circle(2,mode='s').finalize().extrude(-29))