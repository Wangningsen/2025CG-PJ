import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,64))
r=w0.sketch().push([(-48,-80)]).circle(20).reset().face(w0.sketch().segment((-58,-39),(-50,-43)).arc((-39,-35),(-39,-49)).segment((-7,-67)).segment((68,72)).segment((16,100)).close().assemble()).finalize().extrude(-129)