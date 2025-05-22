import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,17))
r=w0.sketch().push([(-36,0)]).circle(64).push([(64,-21)]).rect(10,34).finalize().extrude(-38).union(w0.workplane(offset=4/2).moveTo(64,-21).cylinder(4,36))