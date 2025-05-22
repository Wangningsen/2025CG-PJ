import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-26))
r=w0.sketch().push([(-59,-1)]).circle(41).push([(73,15)]).circle(27).finalize().extrude(53)