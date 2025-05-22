import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-48,0))
w1=cq.Workplane('ZX',origin=(0,-56,0))
r=w0.sketch().push([(-43.5,-53)]).rect(113,90).push([(49,28)]).circle(51).finalize().extrude(105).union(w0.workplane(offset=104/2).moveTo(-59.5,89).box(3,18,104)).union(w1.workplane(offset=2/2).moveTo(49,28).cylinder(2,28))