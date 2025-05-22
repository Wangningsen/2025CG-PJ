import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,29))
w1=cq.Workplane('XY',origin=(0,0,62))
r=w0.sketch().segment((-26,-74),(-22,-74)).segment((-22,-67)).arc((-24,-70),(-26,-74)).assemble().finalize().extrude(-89).union(w1.sketch().segment((-2,-20),(41,-20)).arc((36,-10),(41,1)).segment((8,1)).arc((-95,42),(-2,-16)).close().assemble().reset().face(w1.sketch().segment((58,-20),(100,-20)).segment((100,1)).segment((58,1)).arc((63,-10),(58,-20)).assemble()).finalize().extrude(-33))