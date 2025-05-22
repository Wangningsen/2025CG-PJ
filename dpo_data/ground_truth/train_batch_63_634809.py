import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-100))
w1=cq.Workplane('XY',origin=(0,0,-74))
r=w0.sketch().segment((-67,-46),(-17,-46)).arc((0,-50),(17,-46)).segment((67,-46)).segment((67,20)).segment((17,20)).arc((0,24),(-17,20)).segment((-67,20)).close().assemble().push([(-2,54)]).rect(118,48).finalize().extrude(138).union(w1.sketch().arc((5,-78),(23,-44),(5,-9)).segment((5,-12)).arc((21,-44),(5,-76)).close().assemble().finalize().extrude(174))