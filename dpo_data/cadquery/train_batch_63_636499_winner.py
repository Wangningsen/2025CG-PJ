import cadquery as cq
w0=cq.Workplane('YZ',origin=(-33,0,0))
r=w0.workplane(offset=-49/2).moveTo(83,69).cylinder(49,17).union(w0.workplane(offset=115/2).moveTo(-80,-66).cylinder(115,20))