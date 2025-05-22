import cadquery as cq
w0=cq.Workplane('YZ',origin=(-32,0,0))
w1=cq.Workplane('ZX',origin=(0,-14,0))
r=w0.sketch().segment((-71,-50),(-56,-100)).arc((-49,-75),(-33,-55)).segment((-33,-39)).close().assemble().reset().face(w0.sketch().segment((9,-27),(62,-27)).segment((62,-49)).arc((66,-52),(71,-56)).segment((59,-14)).close().assemble()).finalize().extrude(-47).union(w1.sketch().segment((-1,-77),(80,-77)).segment((80,-44)).arc((100,1),(80,45)).segment((80,79)).segment((-1,79)).segment((-1,45)).arc((-20,1),(-1,-44)).close().assemble().finalize().extrude(4))