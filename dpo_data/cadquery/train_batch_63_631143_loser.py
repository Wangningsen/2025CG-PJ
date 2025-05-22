import cadquery as cq
w0=cq.Workplane('YZ',origin=(-5,0,0))
w1=cq.Workplane('YZ',origin=(1,0,0))
r=w0.workplane(offset=-69/2).moveTo(61,-51).box(22,14,69).union(w0.sketch().segment((-100,-23),(9,-37)).segment((16,28)).segment((15,28)).arc((11,37),(4,38)).segment((-10,40)).arc((-34,-6),(-64,36)).segment((-70,37)).segment((-64,47)).segment((-90,50)).close().assemble().push([(41,36.5)]).rect(16,109).reset().face(w0.sketch().segment((28,-29),(87,-91)).segment((100,-79)).segment((41,-16)).close().assemble()).finalize().extrude(78)).union(w1.workplane(offset=10/2).moveTo(41,37).cylinder(10,5))