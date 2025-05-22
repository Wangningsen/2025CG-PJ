import cadquery as cq
w0=cq.Workplane('YZ',origin=(-19,0,0))
r=w0.sketch().push([(-77,-65)]).circle(23).push([(11,0)]).circle(89).finalize().extrude(38)