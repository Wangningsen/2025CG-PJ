import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-34))
r=w0.sketch().push([(-75,-81)]).circle(19).push([(38.5,39)]).rect(7,122).finalize().extrude(-22).union(w0.workplane(offset=90/2).moveTo(39,39).cylinder(90,55)).union(w0.workplane(offset=90/2).moveTo(39,39).cylinder(90,55))