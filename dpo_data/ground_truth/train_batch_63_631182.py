import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,29))
r=w0.workplane(offset=-118/2).moveTo(75,66).cylinder(118,25).union(w0.sketch().arc((-58,-46),(27,-77),(-1,9)).arc((-85,39),(-58,-46)).assemble().finalize().extrude(59))