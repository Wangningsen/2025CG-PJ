import cadquery as cq
w0=cq.Workplane('YZ',origin=(-100,0,0))
r=w0.sketch().segment((-89,-53),(-80,-64)).segment((-71,-55)).arc((52,-72),(78,44)).segment((89,53)).segment((80,64)).segment((71,55)).arc((-52,72),(-78,-44)).close().assemble().finalize().extrude(200)