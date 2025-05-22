import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,20))
r=w0.sketch().arc((-45,-18),(38,-96),(44,22)).arc((-41,95),(-45,-18)).assemble().push([(-29,-35.5)]).rect(30,53,mode='s').push([(62.5,-35.5)]).rect(31,53,mode='s').finalize().extrude(-66).union(w0.workplane(offset=27/2).moveTo(-66.5,37).box(27,6,27))