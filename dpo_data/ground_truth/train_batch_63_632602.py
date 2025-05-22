import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,63,0))
r=w0.sketch().push([(-13.5,-72)]).rect(75,56).push([(-3,-79)]).circle(2,mode='s').push([(13,62)]).circle(38).finalize().extrude(-127).union(w0.workplane(offset=-14/2).moveTo(-20,-12).box(54,108,14))