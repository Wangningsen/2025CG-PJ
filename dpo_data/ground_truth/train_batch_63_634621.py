import cadquery as cq
w0=cq.Workplane('YZ',origin=(72,0,0))
r=w0.sketch().arc((-99,57),(-65,-3),(-92,-66)).arc((-21,-100),(53,-71)).segment((87,-74)).segment((99,68)).segment((53,72)).arc((-26,100),(-99,57)).assemble().reset().face(w0.sketch().segment((64,-50),(67,-50)).segment((68,48)).segment((65,48)).close().assemble(),mode='s').finalize().extrude(-144)