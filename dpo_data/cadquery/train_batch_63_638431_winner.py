import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-22,0))
r=w0.workplane(offset=-10/2).moveTo(-36,-26).cylinder(10,31).union(w0.sketch().push([(-40,-65)]).circle(35).push([(7.5,76)]).rect(135,48).finalize().extrude(54))