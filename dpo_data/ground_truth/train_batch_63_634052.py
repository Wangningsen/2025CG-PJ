import cadquery as cq
w0=cq.Workplane('YZ',origin=(32,0,0))
r=w0.sketch().arc((-37,59),(-98,-1),(-14,-18)).arc((-81,4),(-37,59)).assemble().reset().face(w0.sketch().arc((0,0),(97,-28),(2,7)).arc((2,3),(0,0)).assemble()).push([(25,-18.5)]).rect(6,63,mode='s').finalize().extrude(-64)