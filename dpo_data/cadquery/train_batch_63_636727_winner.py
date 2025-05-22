import cadquery as cq
w0=cq.Workplane('YZ',origin=(20,0,0))
r=w0.workplane(offset=-71/2).moveTo(18,34).cylinder(71,66).union(w0.sketch().arc((-26,39),(-52,-89),(55,-24)).segment((69,-24)).segment((69,92)).segment((-26,92)).close().assemble().push([(-13,-31)]).circle(27,mode='s').reset().face(w0.sketch().arc((-16,40),(23,30),(48,0)).arc((39,56),(-16,40)).assemble(),mode='s').finalize().extrude(31))