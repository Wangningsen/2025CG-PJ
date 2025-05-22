import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-30))
r=w0.sketch().push([(-24,31)]).circle(7).push([(-6,-13)]).circle(10).push([(69,30)]).rect(62,44).finalize().extrude(31).union(w0.workplane(offset=57/2).moveTo(-68.5,-2.5).box(63,57,57)).union(w0.workplane(offset=59/2).moveTo(48,-29).cylinder(59,23))