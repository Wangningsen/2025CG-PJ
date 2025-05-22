import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,57))
r=w0.workplane(offset=-114/2).moveTo(55.5,21).box(89,130,114).union(w0.workplane(offset=-31/2).moveTo(-82,-69).cylinder(31,18))