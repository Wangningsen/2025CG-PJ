import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,73))
r=w0.sketch().push([(-17,46)]).circle(54).push([(46,-75)]).circle(25).finalize().extrude(-147)