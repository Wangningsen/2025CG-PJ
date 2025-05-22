import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,4,0))
r=w0.sketch().segment((16,17),(20,17)).arc((57,-10),(95,17)).segment((99,17)).segment((99,24)).arc((100,33),(99,42)).segment((99,49)).segment((95,49)).arc((57,76),(20,49)).segment((16,49)).segment((16,42)).arc((14,33),(16,24)).close().assemble().finalize().extrude(-13).union(w0.workplane(offset=5/2).moveTo(-34,-10).cylinder(5,66))