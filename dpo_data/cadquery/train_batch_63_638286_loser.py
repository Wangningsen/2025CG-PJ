import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,43,0))
r=w0.workplane(offset=-86/2).moveTo(-49,26).cylinder(86,19).union(w0.sketch().push([(-44,50)]).circle(50).push([(63,-69)]).circle(31).finalize().extrude(-69)).union(w0.sketch().push([(-48,-40)]).circle(38).push([(-68,-48)]).circle(5,mode='s').push([(-30.5,-29.5)]).rect(5,19,mode='s').finalize().extrude(-28))