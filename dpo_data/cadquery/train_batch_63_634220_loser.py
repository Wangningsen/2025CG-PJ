import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-14,0))
w1=cq.Workplane('ZX',origin=(0,-67,0))
r=w0.sketch().push([(-3,44)]).rect(54,112).push([(-9.5,10.5)]).rect(5,35,mode='s').push([(21,10.5)]).rect(4,35,mode='s').finalize().extrude(-20).union(w0.sketch().segment((43,77),(48,73)).segment((53,77)).close().assemble().finalize().extrude(89)).union(w1.sketch().segment((-49,-100),(-31,-100)).segment((-31,-63)).arc((-26,-53),(-31,-44)).segment((-31,-6)).segment((-49,-6)).segment((-49,-44)).arc((-53,-53),(-49,-63)).close().assemble().finalize().extrude(-8))