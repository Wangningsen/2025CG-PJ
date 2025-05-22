import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,84))
r=w0.workplane(offset=-168/2).moveTo(-57,-18).cylinder(168,5).union(w0.sketch().segment((-58,100),(28,-100)).arc((52,29),(-58,100)).assemble().finalize().extrude(-119))