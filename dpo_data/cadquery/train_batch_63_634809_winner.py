import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-75))
w1=cq.Workplane('XY',origin=(0,0,-100))
r=w0.sketch().arc((5,-78),(23,-43),(5,-7)).segment((5,-18)).arc((20,-43),(5,-68)).close().assemble().finalize().extrude(175).union(w1.sketch().segment((-67,-46),(-17,-46)).arc((0,-50),(17,-46)).segment((67,-46)).segment((67,20)).segment((17,20)).arc((0,24),(-17,20)).segment((-67,20)).close().assemble().push([(-2,54)]).rect(118,48).finalize().extrude(138))