import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,52,0))
w1=cq.Workplane('YZ',origin=(16,0,0))
r=w0.sketch().segment((31,-30),(62,-46)).segment((100,25)).segment((59,46)).segment((84,19)).close().assemble().finalize().extrude(-79).union(w0.sketch().arc((-68,-11),(-41,-6),(-38,21)).close().assemble().finalize().extrude(-60)).union(w1.sketch().segment((-52,-100),(12,-100)).segment((12,-31)).segment((-39,-31)).arc((-45,-30),(-52,-31)).segment((-52,-59)).close().assemble().push([(-19,-66)]).circle(11,mode='s').finalize().extrude(-49))