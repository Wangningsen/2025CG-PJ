import cadquery as cq
w0=cq.Workplane('YZ',origin=(-30,0,0))
r=w0.sketch().push([(-29.5,70)]).rect(43,60).push([(27,-76)]).circle(24).finalize().extrude(59)