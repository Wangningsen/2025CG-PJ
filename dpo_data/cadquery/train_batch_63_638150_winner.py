import cadquery as cq
w0=cq.Workplane('YZ',origin=(-14,0,0))
w1=cq.Workplane('ZX',origin=(0,39,0))
r=w0.sketch().push([(-30,-61.5)]).rect(18,77).push([(18,-61.5)]).rect(18,77).finalize().extrude(78).union(w1.sketch().push([(71,-35)]).circle(29).circle(6,mode='s').finalize().extrude(-13))