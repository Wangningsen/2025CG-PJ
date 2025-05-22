import cadquery as cq
w0=cq.Workplane('YZ',origin=(72,0,0))
w1=cq.Workplane('YZ',origin=(13,0,0))
r=w0.sketch().segment((-100,49),(-13,57)).segment((-16,95)).segment((-100,86)).close().assemble().finalize().extrude(-17).union(w0.sketch().push([(68,-56)]).rect(64,78).reset().face(w0.sketch().segment((60,-82),(62,-82)).segment((62,-76)).arc((87,-56),(62,-36)).segment((62,-28)).segment((60,-28)).segment((60,-36)).arc((36,-56),(60,-76)).close().assemble(),mode='s').finalize().extrude(21)).union(w1.workplane(offset=-106/2).moveTo(32.5,8).box(61,100,106))