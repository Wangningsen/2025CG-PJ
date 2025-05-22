import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,100,0))
r=w0.sketch().segment((-28,-67),(28,-67)).segment((28,-24)).arc((21,-13),(13,-1)).segment((13,-17)).segment((-13,-17)).segment((-13,17)).segment((9,17)).arc((7,41),(10,67)).segment((-28,67)).close().assemble().finalize().extrude(-200)