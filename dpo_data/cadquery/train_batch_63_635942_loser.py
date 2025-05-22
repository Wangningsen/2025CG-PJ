import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-35,0))
r=w0.sketch().push([(-22,40)]).circle(60).push([(-24,-59)]).circle(41).push([(78,9)]).circle(4).finalize().extrude(35).union(w0.workplane(offset=70/2).moveTo(-3,-53).cylinder(70,24))