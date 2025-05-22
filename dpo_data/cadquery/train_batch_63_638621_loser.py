import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,9,0))
w1=cq.Workplane('ZX',origin=(0,15,0))
r=w0.sketch().push([(-88,-96)]).circle(4).push([(42,50)]).circle(50).finalize().extrude(65).union(w0.workplane(offset=65/2).moveTo(42,50).cylinder(65,2)).union(w1.workplane(offset=-90/2).moveTo(42.5,24.5).box(21,17,90))