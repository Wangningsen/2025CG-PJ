import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-24,0))
r=w0.sketch().push([(-44,26)]).circle(48).push([(-21,-47)]).rect(60,106).finalize().extrude(42).union(w0.sketch().segment((-36,-82),(11,-82)).segment((11,-72)).segment((19,-72)).segment((19,-3)).segment((11,-3)).segment((11,6)).segment((-36,6)).close().assemble().push([(49,56)]).circle(44).finalize().extrude(49))