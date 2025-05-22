import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,17))
r=w0.sketch().push([(-37,71)]).circle(29).push([(-37,71.5)]).rect(6,29,mode='s').push([(45,-69.5)]).rect(2,61).finalize().extrude(-34).union(w0.workplane(offset=-8/2).moveTo(47,-9).cylinder(8,19))