import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,36))
r=w0.workplane(offset=-87/2).moveTo(27,58).cylinder(87,42).union(w0.sketch().segment((-31,-100),(-21,-100)).segment((-21,-81)).arc((17,-39),(-21,-2)).segment((-21,11)).segment((-31,11)).segment((-31,-2)).arc((-69,-39),(-31,-81)).close().assemble().finalize().extrude(15))