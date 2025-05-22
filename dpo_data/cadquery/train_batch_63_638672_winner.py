import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-26))
w1=cq.Workplane('ZX',origin=(0,50,0))
r=w0.sketch().segment((-100,27),(5,27)).segment((5,88)).segment((-27,88)).arc((-15,81),(-13,66)).segment((-5,66)).segment((-5,56)).segment((-75,56)).segment((-75,66)).segment((-68,66)).arc((-69,81),(-57,88)).segment((-100,88)).close().assemble().finalize().extrude(-20).union(w1.sketch().segment((-38,47),(-35,47)).segment((-35,-24)).segment((43,-24)).segment((43,47)).segment((46,47)).segment((46,100)).segment((-38,100)).close().assemble().finalize().extrude(-138))