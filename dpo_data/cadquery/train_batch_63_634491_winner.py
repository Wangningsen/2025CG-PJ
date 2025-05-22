import cadquery as cq
w0=cq.Workplane('YZ',origin=(-66,0,0))
r=w0.sketch().segment((-100,-68),(-71,-68)).arc((-35,-83),(2,-68)).segment((31,-68)).segment((31,-9)).arc((78,75),(17,1)).segment((2,1)).arc((-35,15),(-71,1)).segment((-100,1)).close().assemble().push([(51.5,31)]).rect(1,72,mode='s').finalize().extrude(133)