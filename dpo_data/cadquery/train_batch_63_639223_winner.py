import cadquery as cq
w0=cq.Workplane('YZ',origin=(-32,0,0))
w1=cq.Workplane('ZX',origin=(0,-10,0))
r=w0.sketch().segment((-71,-50),(-56,-100)).arc((-50,-78),(-33,-58)).segment((-33,-39)).close().assemble().reset().face(w0.sketch().segment((9,-27),(62,-27)).segment((62,-51)).arc((68,-53),(71,-56)).segment((59,-14)).close().assemble()).finalize().extrude(-47).union(w1.sketch().segment((-1,-77),(80,-77)).segment((80,-47)).arc((100,1),(80,47)).segment((80,79)).segment((-1,79)).segment((-1,47)).arc((-20,1),(-1,-47)).close().assemble().finalize().extrude(-4))