import cadquery as cq
w0=cq.Workplane('YZ',origin=(-72,0,0))
r=w0.sketch().arc((-99,55),(-65,-1),(-92,-66)).arc((-14,-100),(65,-44)).segment((62,-71)).segment((87,-74)).segment((99,68)).segment((54,72)).arc((-23,100),(-99,57)).close().assemble().reset().face(w0.sketch().arc((64,-30),(68,-1),(65,30)).close().assemble(),mode='s').finalize().extrude(144)