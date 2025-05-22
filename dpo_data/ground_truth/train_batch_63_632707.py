import cadquery as cq
w0=cq.Workplane('YZ',origin=(-23,0,0))
w1=cq.Workplane('YZ',origin=(-80,0,0))
r=w0.workplane(offset=104/2).moveTo(-93,17).cylinder(104,7).union(w1.sketch().segment((31,-24),(34,-24)).arc((66,3),(97,-24)).segment((100,-24)).arc((66,6),(31,-24)).assemble().finalize().extrude(33))