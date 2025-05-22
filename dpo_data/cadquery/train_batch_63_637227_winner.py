import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-42,0))
r=w0.workplane(offset=-58/2).moveTo(15,18).cylinder(58,74).union(w0.sketch().push([(-50,-53)]).circle(39).push([(-78.5,-69)]).rect(5,14,mode='s').push([(-53,-50)]).circle(7,mode='s').finalize().extrude(142))