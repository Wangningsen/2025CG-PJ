import cadquery as cq
w0=cq.Workplane('YZ',origin=(22,0,0))
w1=cq.Workplane('YZ',origin=(19,0,0))
r=w0.sketch().segment((7,23),(7,71)).segment((65,71)).arc((-27,-18),(94,23)).close().assemble().finalize().extrude(78).union(w1.sketch().segment((-94,-82),(10,-82)).segment((10,-5)).arc((50,36),(6,-1)).segment((-94,-1)).close().assemble().finalize().extrude(-119))