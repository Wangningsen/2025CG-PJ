import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-80))
r=w0.sketch().push([(13,13)]).rect(138,174).circle(52,mode='s').finalize().extrude(123).union(w0.workplane(offset=160/2).moveTo(0,-12).cylinder(160,88))