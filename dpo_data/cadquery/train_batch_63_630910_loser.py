import cadquery as cq
w0=cq.Workplane('YZ',origin=(-59,0,0))
r=w0.sketch().push([(-91,-16)]).circle(9).reset().face(w0.sketch().segment((-99,-16),(-95,-20)).segment((-87,-14)).segment((-91,-10)).close().assemble(),mode='s').finalize().extrude(13).union(w0.workplane(offset=118/2).moveTo(42.5,0).box(115,100,118))