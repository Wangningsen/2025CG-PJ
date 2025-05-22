import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.workplane(offset=-200/2).moveTo(0,3).cylinder(200,92).union(w0.sketch().segment((-59,-95),(2,-95)).segment((2,-90)).segment((31,-90)).segment((31,-95)).segment((75,-95)).segment((75,-16)).segment((31,-16)).segment((31,-20)).segment((2,-20)).segment((2,-16)).segment((-59,-16)).close().assemble().finalize().extrude(-174))