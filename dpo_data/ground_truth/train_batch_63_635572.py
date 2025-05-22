import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,47,0))
w1=cq.Workplane('ZX',origin=(0,13,0))
r=w0.sketch().push([(-35,-43)]).rect(92,114).push([(45.5,18.5)]).rect(41,105).push([(45.5,54.5)]).rect(25,11,mode='s').finalize().extrude(-129).union(w1.workplane(offset=69/2).moveTo(68,87).cylinder(69,13))