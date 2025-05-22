import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-16,0))
r=w0.sketch().segment((-43,11),(-14,11)).segment((-14,63)).segment((-26,63)).arc((-92,83),(-43,34)).close().assemble().push([(12,-30)]).circle(21).finalize().extrude(-55).union(w0.workplane(offset=39/2).moveTo(-3,9).cylinder(39,1)).union(w0.sketch().push([(70,-72)]).circle(28).circle(1,mode='s').finalize().extrude(87))