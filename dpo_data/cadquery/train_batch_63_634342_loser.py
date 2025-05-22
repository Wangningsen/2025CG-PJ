import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,45))
r=w0.sketch().arc((-46,56),(-38,-45),(34,28)).segment((34,100)).segment((-46,100)).close().assemble().reset().face(w0.sketch().arc((70,-100),(71,-97),(74,-97)).arc((71,-92),(70,-100)).assemble()).finalize().extrude(-90)