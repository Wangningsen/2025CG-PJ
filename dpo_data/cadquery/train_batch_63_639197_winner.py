import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-15))
r=w0.sketch().push([(-36.5,47)]).rect(117,106).push([(92.5,-97)]).rect(5,6).finalize().extrude(30)