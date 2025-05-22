import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-13))
r=w0.workplane(offset=-19/2).moveTo(0,-5.5).box(200,129,19).union(w0.sketch().arc((-17,25),(24,20),(32,-17)).segment((68,28)).segment((19,70)).close().assemble().finalize().extrude(45))