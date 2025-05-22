import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-14))
r=w0.sketch().push([(-49,36)]).rect(102,70).reset().face(w0.sketch().segment((4,-66),(48,-66)).segment((52,-71)).segment((58,-68)).segment((57,-66)).segment((100,-66)).segment((100,-58)).segment((55,-58)).segment((51,-52)).segment((45,-55)).segment((46,-58)).segment((4,-58)).close().assemble()).finalize().extrude(28)