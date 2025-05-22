import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-88,0))
w1=cq.Workplane('XY',origin=(0,0,-26))
r=w0.sketch().segment((-38,47),(-35,47)).segment((-35,-24)).segment((43,-24)).segment((43,47)).segment((46,47)).segment((46,100)).segment((-38,100)).close().assemble().finalize().extrude(138).union(w1.sketch().segment((-100,35),(-98,35)).segment((-98,27)).segment((-19,27)).segment((-19,35)).segment((5,35)).segment((5,88)).segment((-28,88)).arc((-15,68),(-19,45)).segment((-19,56)).segment((-80,56)).arc((-79,74),(-68,88)).segment((-100,88)).close().assemble().finalize().extrude(-20))