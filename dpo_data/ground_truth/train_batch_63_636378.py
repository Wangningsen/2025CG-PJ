import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,46))
r=w0.workplane(offset=-114/2).moveTo(-21.5,84).box(115,32,114).union(w0.workplane(offset=-97/2).moveTo(66,-10).cylinder(97,13)).union(w0.sketch().segment((-67,-100),(-36,-100)).segment((-36,11)).segment((-67,11)).segment((-67,0)).arc((-66,-2),(-67,-2)).close().assemble().finalize().extrude(22))