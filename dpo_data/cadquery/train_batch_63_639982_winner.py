import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,28,0))
w1=cq.Workplane('ZX',origin=(0,42,0))
r=w0.workplane(offset=20/2).moveTo(-51,-4.5).box(76,27,20).union(w0.sketch().push([(8,-72)]).circle(28).push([(56,67)]).circle(33).finalize().extrude(48)).union(w1.sketch().arc((-32,-59),(18,-63),(33,-15)).arc((35,6),(28,27)).segment((66,27)).segment((66,40)).segment((17,40)).arc((-74,24),(-32,-59)).assemble().finalize().extrude(-118))