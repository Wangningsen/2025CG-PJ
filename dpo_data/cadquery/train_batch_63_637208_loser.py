import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-13))
r=w0.workplane(offset=-19/2).moveTo(0,-5.5).box(200,129,19).union(w0.sketch().segment((-17,26),(17,26)).segment((17,22)).arc((32,7),(31,-14)).segment((68,28)).segment((18,70)).close().assemble().finalize().extrude(45))