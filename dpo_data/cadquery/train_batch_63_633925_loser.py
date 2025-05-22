import cadquery as cq
w0=cq.Workplane('YZ',origin=(-42,0,0))
w1=cq.Workplane('YZ',origin=(-43,0,0))
r=w0.sketch().segment((-41,-46),(48,-49)).segment((48,-33)).segment((44,-33)).segment((44,-13)).segment((48,-13)).segment((48,-10)).segment((56,-10)).segment((56,0)).segment((59,0)).segment((60,27)).segment((48,27)).segment((48,39)).segment((31,39)).segment((31,28)).segment((-24,29)).arc((-91,69),(-39,13)).close().assemble().finalize().extrude(-33).union(w0.workplane(offset=117/2).moveTo(72,-56).cylinder(117,28)).union(w1.workplane(offset=118/2).moveTo(72,-56).cylinder(118,28))