import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,21,0))
w1=cq.Workplane('YZ',origin=(-4,0,0))
r=w0.sketch().push([(-35,-29)]).circle(65).push([(61,-16)]).circle(45).push([(32,6)]).circle(13,mode='s').push([(54,16.5)]).rect(20,15,mode='s').finalize().extrude(-46).union(w1.workplane(offset=97/2).moveTo(3,-42).cylinder(97,23))