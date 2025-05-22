import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,17))
r=w0.workplane(offset=-117/2).moveTo(19,41).cylinder(117,29).union(w0.sketch().arc((-51,-27),(39,16),(-19,-66)).segment((-1,-45)).arc((18,-1),(-24,-18)).close().assemble().finalize().extrude(83))