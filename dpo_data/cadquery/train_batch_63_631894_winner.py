import cadquery as cq
w0=cq.Workplane('YZ',origin=(4,0,0))
r=w0.sketch().push([(-69,-32.5)]).rect(62,77).push([(-16,39)]).circle(14).push([(81,50.5)]).rect(38,41).finalize().extrude(-33).union(w0.workplane(offset=25/2).moveTo(30,18).cylinder(25,25))