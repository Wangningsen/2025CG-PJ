import cadquery as cq
w0=cq.Workplane('YZ',origin=(-42,0,0))
r=w0.sketch().segment((-41,-46),(57,-49)).segment((58,-41)).arc((44,-19),(59,2)).segment((60,27)).segment((44,27)).segment((44,39)).segment((31,38)).segment((31,28)).segment((-24,29)).arc((-91,70),(-39,11)).close().assemble().finalize().extrude(-33).union(w0.workplane(offset=118/2).moveTo(72,-56).cylinder(118,28))