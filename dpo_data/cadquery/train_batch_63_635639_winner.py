import cadquery as cq
w0=cq.Workplane('YZ',origin=(16,0,0))
w1=cq.Workplane('YZ',origin=(16,0,0))
r=w0.sketch().push([(-41,-47)]).circle(53).reset().face(w0.sketch().segment((-23,25),(-23,100)).arc((-46,63),(-23,25)).assemble()).reset().face(w0.sketch().arc((12,25),(36,63),(12,100)).close().assemble()).finalize().extrude(-31).union(w0.sketch().segment((79,-65),(94,-65)).segment((94,21)).segment((79,21)).segment((79,15)).arc((70,6),(79,-3)).close().assemble().push([(81,-6)]).circle(3,mode='s').finalize().extrude(-24)).union(w1.workplane(offset=-22/2).moveTo(86,-17).cylinder(22,2))