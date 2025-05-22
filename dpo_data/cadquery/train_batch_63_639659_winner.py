import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-100,0))
r=w0.sketch().segment((-28,-67),(28,-67)).segment((28,-24)).segment((13,3)).segment((13,-17)).segment((-13,-17)).segment((-13,17)).segment((9,17)).segment((7,38)).segment((7,53)).segment((10,67)).segment((-28,67)).close().assemble().finalize().extrude(200)