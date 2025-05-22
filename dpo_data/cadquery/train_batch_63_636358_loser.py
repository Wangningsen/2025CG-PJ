import cadquery as cq
w0=cq.Workplane('YZ',origin=(-61,0,0))
r=w0.sketch().push([(-96,76)]).circle(4).push([(45,-27)]).circle(55).push([(92,75)]).circle(7).finalize().extrude(122)