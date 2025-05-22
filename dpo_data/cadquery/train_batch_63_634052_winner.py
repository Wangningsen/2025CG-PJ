import cadquery as cq
w0=cq.Workplane('YZ',origin=(32,0,0))
r=w0.sketch().arc((-37,59),(-99,3),(-19,-21)).arc((-82,9),(-37,59)).assemble().reset().face(w0.sketch().arc((1,-25),(100,-10),(2,7)).arc((-1,-9),(1,-25)).assemble()).push([(25,-18.5)]).rect(6,63,mode='s').finalize().extrude(-64)