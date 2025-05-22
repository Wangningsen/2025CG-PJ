import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-43))
r=w0.sketch().segment((-100,-86),(19,-86)).segment((19,-63)).segment((100,-53)).segment((95,-15)).segment((81,-17)).arc((32,86),(-29,-10)).segment((-100,-10)).close().assemble().reset().face(w0.sketch().segment((45,-57),(66,-57)).segment((66,-32)).arc((56,-38),(45,-42)).close().assemble(),mode='s').finalize().extrude(86)