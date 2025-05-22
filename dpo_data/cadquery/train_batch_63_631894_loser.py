import cadquery as cq
w0=cq.Workplane('YZ',origin=(5,0,0))
r=w0.sketch().push([(-69,-32.5)]).rect(62,77).push([(-16,39)]).circle(14).push([(81,50.5)]).rect(38,41).finalize().extrude(-34).union(w0.workplane(offset=24/2).moveTo(30,18).cylinder(24,25))