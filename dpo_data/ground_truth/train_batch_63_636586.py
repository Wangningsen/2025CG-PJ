import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,1,0))
r=w0.sketch().arc((-44,-32),(0,-76),(60,-61)).arc((93,24),(5,47)).arc((-92,52),(-44,-32)).assemble().reset().face(w0.sketch().arc((-32,-31),(-8,-60),(30,-65)).arc((0,-52),(-19,-25)).arc((-25,-28),(-32,-31)).assemble(),mode='s').finalize().extrude(-2)