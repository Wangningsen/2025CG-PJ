import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-63))
w1=cq.Workplane('YZ',origin=(-48,0,0))
r=w0.sketch().segment((-79,35),(-43,-32)).segment((-9,-14)).arc((-43,11),(-45,53)).close().assemble().push([(0,34)]).rect(66,6).reset().face(w0.sketch().arc((9,82),(43,57),(45,15)).segment((79,33)).segment((43,100)).close().assemble()).finalize().extrude(28).union(w1.sketch().segment((-100,15),(-54,15)).segment((-54,63)).segment((-75,63)).arc((-73,33),(-100,21)).close().assemble().finalize().extrude(48))