import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-4))
r=w0.sketch().push([(-70,58.5)]).rect(36,83).reset().face(w0.sketch().segment((-54,-83),(21,-81)).arc((46,-100),(68,-80)).segment((88,-79)).segment((88,-76)).segment((68,-77)).arc((43,-52),(21,-78)).segment((-54,-81)).close().assemble()).finalize().extrude(8)