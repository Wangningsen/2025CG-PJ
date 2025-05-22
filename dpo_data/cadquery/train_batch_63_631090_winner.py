import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-29))
w1=cq.Workplane('ZX',origin=(0,4,0))
r=w0.sketch().arc((-8,76),(-66,11),(20,-8)).segment((21,-8)).segment((21,-4)).segment((61,-4)).segment((61,24)).arc((69,48),(61,72)).segment((61,100)).segment((-8,100)).close().assemble().finalize().extrude(-45).union(w1.workplane(offset=-104/2).moveTo(30,15.5).box(86,21,104))