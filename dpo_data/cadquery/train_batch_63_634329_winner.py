import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-11))
w1=cq.Workplane('XY',origin=(0,0,-12))
r=w0.sketch().push([(-75,-47)]).circle(25).push([(68.5,43)]).rect(63,28).push([(72,43)]).circle(3,mode='s').finalize().extrude(-47).union(w0.sketch().push([(-66.5,12)]).rect(39,26).push([(-66.5,11.5)]).rect(25,21,mode='s').finalize().extrude(-31)).union(w1.workplane(offset=70/2).moveTo(1,32.5).box(34,79,70))