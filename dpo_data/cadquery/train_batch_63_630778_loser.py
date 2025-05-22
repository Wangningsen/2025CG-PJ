import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,69))
r=w0.sketch().push([(-64,49)]).circle(36).push([(86,-71)]).circle(14).finalize().extrude(-138)