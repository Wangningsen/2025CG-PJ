import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,46))
r=w0.workplane(offset=-92/2).moveTo(64,-13).cylinder(92,29).union(w0.sketch().push([(-77,19)]).circle(23).push([(86,11)]).circle(14).finalize().extrude(-91))