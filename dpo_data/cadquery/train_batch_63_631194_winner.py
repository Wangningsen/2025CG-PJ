import cadquery as cq
w0=cq.Workplane('YZ',origin=(-46,0,0))
r=w0.sketch().push([(-58,97)]).circle(3).reset().face(w0.sketch().segment((-39,-67),(-34,-67)).arc((0,-100),(35,-67)).segment((61,-67)).segment((61,-12)).segment((-39,-12)).close().assemble()).finalize().extrude(93)