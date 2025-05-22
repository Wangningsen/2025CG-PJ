import cadquery as cq
w0=cq.Workplane('YZ',origin=(6,0,0))
r=w0.sketch().segment((-43,0),(-42,-78)).segment((31,-78)).segment((31,-46)).arc((36,-49),(42,-50)).segment((42,-45)).segment((45,-45)).segment((45,-50)).arc((99,-4),(28,7)).arc((8,17),(-16,14)).segment((-28,14)).arc((-83,70),(-43,2)).close().assemble().finalize().extrude(-12)