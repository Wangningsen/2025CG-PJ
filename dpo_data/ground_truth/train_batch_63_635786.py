import cadquery as cq
w0=cq.Workplane('YZ',origin=(22,0,0))
w1=cq.Workplane('XY',origin=(0,0,-60))
r=w0.sketch().arc((-45,-90),(-38,-94),(-30,-96)).arc((45,90),(-45,-90)).assemble().finalize().extrude(-121).union(w1.sketch().arc((69,-95),(80,-83),(90,-69)).segment((81,-69)).segment((81,-57)).segment((94,-57)).arc((96,-5),(69,40)).close().assemble().finalize().extrude(33))