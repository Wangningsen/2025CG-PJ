import cadquery as cq
w0=cq.Workplane('YZ',origin=(31,0,0))
w1=cq.Workplane('YZ',origin=(35,0,0))
r=w0.sketch().arc((51,88),(61,67),(64,42)).arc((99,77),(51,88)).assemble().finalize().extrude(59).union(w0.sketch().segment((-100,-94),(-82,-94)).arc((-72,-97),(-62,-94)).segment((-44,-94)).segment((-44,-67)).segment((-62,-67)).arc((-72,-63),(-82,-67)).segment((-100,-67)).close().assemble().finalize().extrude(65)).union(w1.workplane(offset=-130/2).moveTo(-72,-80).cylinder(130,18))