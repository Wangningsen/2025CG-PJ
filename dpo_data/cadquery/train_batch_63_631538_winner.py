import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,56,0))
w1=cq.Workplane('ZX',origin=(0,10,0))
r=w0.sketch().push([(-43.5,-53)]).rect(113,90).push([(49,28)]).circle(51).finalize().extrude(-105).union(w1.workplane(offset=-67/2).moveTo(-57.5,89).box(7,18,67))