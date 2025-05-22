import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,21))
r=w0.sketch().push([(-92,-7)]).circle(8).reset().face(w0.sketch().segment((11,2),(57,-49)).arc((20,39),(96,-20)).segment((47,33)).close().assemble()).finalize().extrude(-42)