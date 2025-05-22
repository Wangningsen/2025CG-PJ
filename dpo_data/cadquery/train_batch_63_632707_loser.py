import cadquery as cq
w0=cq.Workplane('YZ',origin=(-47,0,0))
w1=cq.Workplane('YZ',origin=(-24,0,0))
r=w0.sketch().segment((31,-24),(33,-24)).arc((65,3),(97,-24)).segment((100,-24)).arc((65,6),(31,-24)).assemble().finalize().extrude(-34).union(w1.workplane(offset=105/2).moveTo(-93,17).cylinder(105,7))