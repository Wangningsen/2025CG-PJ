import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,10,0))
r=w0.sketch().segment((-96,34),(-90,34)).segment((-90,50)).arc((-85,57),(-90,64)).segment((-90,80)).segment((-96,80)).segment((-96,64)).arc((-100,57),(-96,50)).close().assemble().push([(-9,-49)]).rect(50,62).reset().face(w0.sketch().segment((23,-41),(80,-77)).segment((100,-45)).segment((43,-9)).close().assemble()).finalize().extrude(-21)