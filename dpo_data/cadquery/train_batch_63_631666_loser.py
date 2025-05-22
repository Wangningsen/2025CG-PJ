import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,20))
r=w0.workplane(offset=-120/2).moveTo(0,40).cylinder(120,57).union(w0.sketch().push([(0.5,-67)]).rect(83,60).push([(0,39.5)]).rect(18,69).finalize().extrude(80))