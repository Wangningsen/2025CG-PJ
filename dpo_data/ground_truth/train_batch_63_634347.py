import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-19))
r=w0.sketch().push([(-27,11)]).circle(73).push([(85,-69)]).circle(15).finalize().extrude(38)