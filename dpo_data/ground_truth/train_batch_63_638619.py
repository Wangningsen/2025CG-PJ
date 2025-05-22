import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,9))
r=w0.sketch().push([(-40,85)]).circle(15).push([(31,-76)]).circle(24).finalize().extrude(-18)