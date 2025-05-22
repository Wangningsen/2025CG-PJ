import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-100))
w1=cq.Workplane('ZX',origin=(0,26,0))
r=w0.sketch().push([(25,-30)]).rect(78,18).push([(25,18)]).rect(78,18).finalize().extrude(77).union(w1.sketch().push([(71,-35)]).circle(29).circle(6,mode='s').finalize().extrude(13))