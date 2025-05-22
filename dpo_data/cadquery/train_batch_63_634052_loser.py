import cadquery as cq
w0=cq.Workplane('YZ',origin=(32,0,0))
r=w0.sketch().arc((-37,59),(-100,11),(-31,-31)).arc((-82,13),(-37,59)).assemble().reset().face(w0.sketch().arc((2,-28),(100,-10),(2,8)).arc((0,-10),(2,-28)).assemble()).push([(25,-15)]).rect(6,60,mode='s').finalize().extrude(-64)