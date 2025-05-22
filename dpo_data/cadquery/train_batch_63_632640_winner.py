import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-41,0))
w1=cq.Workplane('ZX',origin=(0,-61,0))
r=w0.sketch().arc((-99,-14),(-29,-31),(-32,-95)).arc((76,65),(-99,-14)).assemble().finalize().extrude(110).union(w1.sketch().push([(0,0)]).rect(106,164).reset().face(w1.sketch().segment((-37,-60),(29,-60)).segment((29,-45)).arc((34,-29),(29,-14)).segment((29,60)).segment((-37,60)).close().assemble(),mode='s').finalize().extrude(-8))