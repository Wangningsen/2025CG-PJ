import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-87))
r=w0.sketch().push([(-60.5,0)]).rect(79,14).push([(60.5,0)]).rect(79,14).finalize().extrude(175)