import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,27))
r=w0.sketch().arc((-99,-100),(-46,-82),(6,-100)).segment((99,-100)).segment((99,100)).segment((-99,100)).close().assemble().reset().face(w0.sketch().segment((-86,18),(-32,-88)).segment((86,-18)).segment((32,88)).close().assemble(),mode='s').finalize().extrude(-53)