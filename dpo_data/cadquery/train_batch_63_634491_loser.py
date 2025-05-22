import cadquery as cq
w0=cq.Workplane('YZ',origin=(-67,0,0))
r=w0.sketch().segment((-100,-68),(-71,-68)).arc((-35,-83),(1,-68)).segment((31,-68)).segment((31,-9)).arc((47,-14),(64,-12)).arc((66,-11),(67,-12)).arc((66,81),(11,1)).arc((8,-1),(4,-1)).arc((-35,15),(-71,-1)).segment((-100,-1)).close().assemble().push([(51.5,33)]).rect(1,84,mode='s').finalize().extrude(133)