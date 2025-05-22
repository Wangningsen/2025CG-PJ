import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,100,0))
r=w0.sketch().segment((-80,-46),(-78,-46)).segment((-78,-59)).segment((78,-59)).segment((78,-46)).segment((80,-46)).segment((80,46)).segment((78,46)).segment((78,59)).segment((-78,59)).segment((-78,46)).segment((-80,46)).close().assemble().finalize().extrude(-200)