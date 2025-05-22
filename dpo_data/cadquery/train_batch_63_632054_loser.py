import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-48))
r=w0.sketch().segment((-81,39),(-73,50)).arc((-72,50),(-71,51)).arc((-32,43),(-18,78)).arc((-60,97),(-78,55)).segment((-75,54)).arc((-74,53),(-72,50)).segment((-81,41)).close().assemble().reset().face(w0.sketch().segment((7,-85),(42,-100)).segment((81,-7)).segment((45,8)).close().assemble()).finalize().extrude(96)