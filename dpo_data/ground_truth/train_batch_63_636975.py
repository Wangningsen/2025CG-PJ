import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-14))
r=w0.sketch().push([(-49,36)]).rect(102,70).reset().face(w0.sketch().segment((4,-66),(49,-66)).segment((52,-71)).segment((60,-67)).segment((59,-66)).segment((100,-66)).segment((100,-58)).segment((55,-58)).segment((52,-52)).segment((44,-57)).segment((45,-58)).segment((4,-58)).close().assemble()).finalize().extrude(28)