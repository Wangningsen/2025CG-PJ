import cadquery as cq
w0=cq.Workplane('YZ',origin=(14,0,0))
r=w0.sketch().push([(-79,62)]).circle(21).push([(61,-44)]).circle(39).finalize().extrude(-29)