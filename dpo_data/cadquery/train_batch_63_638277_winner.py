import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-46))
w1=cq.Workplane('ZX',origin=(0,-49,0))
r=w0.sketch().arc((-29,-23),(-100,-38),(-29,-50)).close().assemble().push([(-16,-8.5)]).rect(26,95).finalize().extrude(93).union(w1.workplane(offset=122/2).moveTo(28,78).box(10,44,122))