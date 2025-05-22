import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-12))
w1=cq.Workplane('ZX',origin=(0,-24,0))
r=w0.sketch().segment((-49,52),(-29,52)).segment((-29,41)).segment((-9,41)).segment((-9,52)).segment((11,52)).segment((11,71)).segment((-9,71)).segment((-9,78)).segment((-20,86)).segment((-19,88)).segment((-20,88)).segment((-20,100)).segment((-29,100)).segment((-29,89)).segment((-49,89)).close().assemble().finalize().extrude(-15).union(w1.sketch().push([(2.5,20)]).rect(49,58).push([(0,44)]).circle(5,mode='s').finalize().extrude(-76))