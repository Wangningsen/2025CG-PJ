import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,32,0))
r=w0.sketch().push([(-42,-38)]).circle(58).reset().face(w0.sketch().segment((45,13),(56,-62)).segment((93,-57)).segment((83,19)).arc((51,95),(45,13)).assemble()).reset().face(w0.sketch().segment((40,90),(66,14)).segment((76,17)).segment((49,93)).close().assemble(),mode='s').finalize().extrude(-65)