import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,95))
w1=cq.Workplane('XY',origin=(0,0,100))
r=w0.workplane(offset=-195/2).box(108,174,195).union(w1.sketch().segment((-48,-29),(-19,-29)).segment((-19,-37)).segment((-17,-37)).arc((-28,37),(25,-17)).segment((25,-29)).segment((30,-29)).segment((30,29)).segment((-48,29)).close().assemble().finalize().extrude(-82))