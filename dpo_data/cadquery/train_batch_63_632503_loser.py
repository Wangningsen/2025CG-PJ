import cadquery as cq
w0=cq.Workplane('YZ',origin=(57,0,0))
r=w0.sketch().segment((-73,-23),(-6,-100)).segment((74,-31)).segment((36,14)).arc((73,55),(27,84)).arc((-14,98),(-47,75)).arc((-73,47),(-63,9)).arc((-60,0),(-56,-7)).close().assemble().finalize().extrude(-115)