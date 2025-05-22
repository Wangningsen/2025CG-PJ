import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,29))
w1=cq.Workplane('XY',origin=(0,0,30))
r=w0.workplane(offset=-117/2).moveTo(75,66).cylinder(117,25).union(w0.sketch().arc((-58,-46),(28,-76),(-2,9)).arc((-85,39),(-58,-46)).assemble().finalize().extrude(59)).union(w1.workplane(offset=-117/2).moveTo(75,66).cylinder(117,23))