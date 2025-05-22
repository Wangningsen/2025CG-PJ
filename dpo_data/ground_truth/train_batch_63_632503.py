import cadquery as cq
w0=cq.Workplane('YZ',origin=(57,0,0))
r=w0.sketch().segment((-73,-22),(-6,-100)).segment((74,-31)).segment((36,14)).arc((73,54),(27,84)).arc((-2,100),(-32,85)).arc((-73,47),(-54,-5)).close().assemble().finalize().extrude(-115)