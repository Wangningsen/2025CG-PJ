import cadquery as cq
w0=cq.Workplane('YZ',origin=(31,0,0))
r=w0.sketch().arc((2,-91),(8,-73),(22,-60)).arc((-68,-24),(2,-91)).assemble().finalize().extrude(-62).union(w0.sketch().segment((47,50),(47,100)).arc((25,75),(47,50)).assemble().reset().face(w0.sketch().arc((54,50),(76,75),(54,100)).close().assemble()).finalize().extrude(-62))