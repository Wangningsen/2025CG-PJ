import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.sketch().segment((-88,-50),(-80,-64)).segment((-70,-57)).arc((51,-73),(76,46)).segment((88,52)).segment((80,64)).segment((70,57)).arc((-51,73),(-76,-46)).close().assemble().finalize().extrude(-200)