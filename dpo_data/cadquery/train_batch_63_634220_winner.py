import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-14,0))
w1=cq.Workplane('ZX',origin=(0,-68,0))
r=w0.sketch().push([(-3,44)]).rect(54,112).push([(-9.5,7.5)]).rect(5,39,mode='s').push([(21,16)]).circle(3,mode='s').finalize().extrude(-20).union(w0.sketch().arc((43,77),(48,75),(53,77)).close().assemble().finalize().extrude(89)).union(w1.sketch().segment((-49,-100),(-31,-100)).segment((-31,-61)).arc((-26,-53),(-31,-45)).segment((-31,-6)).segment((-49,-6)).segment((-49,-45)).arc((-53,-53),(-49,-61)).close().assemble().finalize().extrude(-6))