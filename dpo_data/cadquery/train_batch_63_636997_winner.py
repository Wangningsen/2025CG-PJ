import cadquery as cq
w0=cq.Workplane('YZ',origin=(8,0,0))
w1=cq.Workplane('XY',origin=(0,0,-16))
r=w0.workplane(offset=-69/2).moveTo(32.5,85).box(39,30,69).union(w0.sketch().segment((-28,-24),(57,-24)).segment((57,50)).segment((12,50)).arc((0,24),(-28,27)).close().assemble().finalize().extrude(-33)).union(w1.workplane(offset=-84/2).moveTo(12,-1.5).box(98,111,84))