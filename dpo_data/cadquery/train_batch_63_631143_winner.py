import cadquery as cq
w0=cq.Workplane('YZ',origin=(-5,0,0))
w1=cq.Workplane('YZ',origin=(20,0,0))
r=w0.sketch().segment((-100,-23),(9,-37)).segment((17,36)).segment((-9,40)).arc((-36,-6),(-64,47)).segment((-90,50)).close().assemble().reset().face(w0.sketch().segment((23,-26),(86,-91)).segment((100,-78)).segment((40,-15)).segment((52,-15)).segment((52,8)).segment((49,8)).segment((49,58)).segment((52,58)).segment((52,91)).segment((31,91)).segment((31,-15)).segment((34,-15)).close().assemble()).finalize().extrude(78).union(w1.workplane(offset=-94/2).moveTo(61.5,-51).box(21,14,94))