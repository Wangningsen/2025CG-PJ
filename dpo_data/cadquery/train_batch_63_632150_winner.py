import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-2,0))
w1=cq.Workplane('ZX',origin=(0,38,0))
r=w0.workplane(offset=-36/2).moveTo(-53,0).cylinder(36,47).union(w1.sketch().segment((41,-24),(61,-24)).segment((61,-32)).segment((80,-32)).segment((80,-24)).segment((100,-24)).segment((100,1)).segment((80,1)).segment((80,9)).segment((61,9)).segment((61,1)).segment((41,1)).close().assemble().finalize().extrude(-47))