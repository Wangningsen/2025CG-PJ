import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-29))
r=w0.sketch().segment((-31,36),(-7,-24)).segment((1,-21)).segment((-22,39)).close().assemble().push([(69,30)]).rect(62,44).finalize().extrude(30).union(w0.sketch().push([(-68.5,-2.5)]).rect(63,57).push([(-15,7)]).circle(8).finalize().extrude(57)).union(w0.workplane(offset=59/2).moveTo(48,-29).cylinder(59,23))