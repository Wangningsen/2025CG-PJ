import cadquery as cq
w0=cq.Workplane('YZ',origin=(57,0,0))
r=w0.sketch().segment((-73,-22),(-6,-100)).segment((74,-31)).segment((36,14)).arc((73,56),(26,84)).arc((-5,100),(-34,83)).arc((-73,47),(-54,-5)).close().assemble().finalize().extrude(-115)