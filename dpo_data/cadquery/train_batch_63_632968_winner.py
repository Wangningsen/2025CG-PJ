import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,68,0))
w1=cq.Workplane('ZX',origin=(0,44,0))
r=w0.sketch().push([(-18,-12.5)]).rect(78,121).push([(14,-19)]).circle(7,mode='s').finalize().extrude(-135).union(w1.sketch().arc((-88,24),(-74,-67),(11,-85)).segment((100,-85)).segment((100,42)).segment((37,42)).arc((9,65),(-26,71)).arc((-81,85),(-88,24)).assemble().finalize().extrude(21))