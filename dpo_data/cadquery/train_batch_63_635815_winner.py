import cadquery as cq
w0=cq.Workplane('YZ',origin=(40,0,0))
r=w0.sketch().segment((-33,-22),(-3,-22)).segment((-33,2)).close().assemble().finalize().extrude(-140).union(w0.sketch().segment((-20,2),(31,-10)).segment((29,-15)).segment((30,-15)).arc((33,-1),(28,13)).arc((11,15),(-5,22)).arc((-15,14),(-20,2)).assemble().finalize().extrude(60))