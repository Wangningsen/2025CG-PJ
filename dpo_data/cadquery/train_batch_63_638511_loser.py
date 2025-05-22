import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,26))
r=w0.sketch().arc((-35,24),(-100,-1),(-36,-25)).arc((100,1),(-35,24)).assemble().reset().face(w0.sketch().arc((-39,18),(-95,-1),(-38,-17)).arc((-40,1),(-39,18)).assemble(),mode='s').finalize().extrude(-52)