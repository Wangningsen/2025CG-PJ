import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.workplane(offset=-200/2).moveTo(0,3).cylinder(200,92).union(w0.sketch().segment((-59,-95),(75,-95)).segment((75,5)).segment((30,5)).segment((30,24)).segment((-59,24)).close().assemble().push([(8,-45)]).rect(4,88,mode='s').finalize().extrude(-174))