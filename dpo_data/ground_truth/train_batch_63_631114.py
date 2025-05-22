import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.sketch().segment((-88,-53),(-80,-64)).segment((-69,-56)).arc((51,-73),(77,45)).segment((88,53)).segment((80,64)).segment((69,56)).arc((-51,73),(-77,-45)).close().assemble().finalize().extrude(-200)