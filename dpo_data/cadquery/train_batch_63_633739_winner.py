import cadquery as cq
w0=cq.Workplane('YZ',origin=(-38,0,0))
w1=cq.Workplane('ZX',origin=(0,-24,0))
r=w0.sketch().push([(6,-10)]).circle(34).push([(41.5,63)]).rect(51,74).finalize().extrude(58).union(w0.workplane(offset=76/2).moveTo(-2.5,-75.5).box(3,49,76)).union(w1.sketch().arc((-11,-19),(-9,-18),(-11,-17)).close().assemble().finalize().extrude(-43))