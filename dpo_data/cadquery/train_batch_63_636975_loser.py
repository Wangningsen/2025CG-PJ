import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,14))
r=w0.sketch().push([(-49,36)]).rect(102,70).reset().face(w0.sketch().segment((4,-66),(45,-66)).arc((52,-71),(60,-66)).segment((100,-66)).segment((100,-58)).segment((60,-58)).arc((52,-52),(45,-58)).segment((4,-58)).close().assemble()).finalize().extrude(-28)