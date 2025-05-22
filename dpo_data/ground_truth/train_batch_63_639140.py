import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-36,0))
r=w0.workplane(offset=27/2).moveTo(52,-15).cylinder(27,48).union(w0.sketch().arc((-13,33),(-99,-6),(-5,-18)).segment((0,-24)).segment((32,3)).arc((69,3),(47,33)).segment((22,63)).close().assemble().push([(50.5,12.5)]).rect(23,21,mode='s').finalize().extrude(71))