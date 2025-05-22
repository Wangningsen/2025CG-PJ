import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-65))
r=w0.sketch().push([(-48,-80)]).circle(20).reset().face(w0.sketch().segment((-58,-38),(-7,-67)).segment((68,72)).segment((16,100)).close().assemble()).finalize().extrude(130)