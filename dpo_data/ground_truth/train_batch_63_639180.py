import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,56,0))
r=w0.sketch().segment((-42,-68),(-28,-100)).segment((38,-71)).segment((37,-70)).arc((3,100),(-42,-68)).assemble().finalize().extrude(-128).union(w0.sketch().segment((-59,-2),(-35,-38)).segment((59,24)).segment((35,60)).close().assemble().finalize().extrude(15))