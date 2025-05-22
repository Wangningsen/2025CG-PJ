import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,25))
r=w0.sketch().arc((-38,-18),(100,-3),(-37,21)).arc((-100,3),(-38,-18)).assemble().reset().face(w0.sketch().arc((-40,-10),(-40,1),(-39,13)).arc((-95,3),(-40,-10)).assemble(),mode='s').finalize().extrude(-51)