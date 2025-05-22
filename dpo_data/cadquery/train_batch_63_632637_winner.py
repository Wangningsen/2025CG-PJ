import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-30))
r=w0.sketch().segment((-31,36),(-7,-24)).segment((-2,-22)).segment((-26,38)).close().assemble().push([(69,30)]).rect(62,44).finalize().extrude(31).union(w0.workplane(offset=57/2).moveTo(-68.5,-2.5).box(63,57,57)).union(w0.sketch().push([(-15,7)]).circle(8).push([(48,-29)]).circle(23).finalize().extrude(59))