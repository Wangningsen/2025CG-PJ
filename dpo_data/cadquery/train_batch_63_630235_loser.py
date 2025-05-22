import cadquery as cq
w0=cq.Workplane('YZ',origin=(-40,0,0))
w1=cq.Workplane('YZ',origin=(-45,0,0))
r=w0.sketch().segment((-29,-24),(-27,-32)).arc((-26,-28),(-24,-24)).close().assemble().finalize().extrude(99).union(w1.sketch().segment((-100,-53),(-49,-53)).segment((-49,-45)).arc((-31,-48),(-13,-48)).arc((100,2),(-18,44)).arc((-64,30),(-81,-11)).segment((-100,-11)).close().assemble().reset().face(w1.sketch().arc((51,37),(-3,-2),(59,-31)).segment((59,-50)).segment((65,-50)).segment((65,-26)).arc((69,-8),(65,9)).segment((65,37)).close().assemble(),mode='s').finalize().extrude(-13))