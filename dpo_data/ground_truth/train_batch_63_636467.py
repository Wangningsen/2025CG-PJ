import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-41,0))
w1=cq.Workplane('ZX',origin=(0,-29,0))
r=w0.sketch().push([(43.5,-97.5)]).rect(9,5).reset().face(w0.sketch().arc((44,-99),(48,-98),(45,-96)).arc((42,-97),(44,-99)).assemble(),mode='s').finalize().extrude(82).union(w1.workplane(offset=67/2).moveTo(-1.5,54.5).box(93,91,67))