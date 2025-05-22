import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-1))
r=w0.sketch().push([(-15.5,-79)]).rect(15,42).push([(6,82)]).circle(18).finalize().extrude(2)