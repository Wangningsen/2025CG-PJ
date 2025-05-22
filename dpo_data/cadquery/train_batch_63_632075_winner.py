import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-7))
w1=cq.Workplane('YZ',origin=(-64,0,0))
r=w0.sketch().arc((71,72),(-82,-58),(94,34)).segment((94,85)).segment((71,85)).close().assemble().reset().face(w0.sketch().arc((-12,51),(20,-82),(51,52)).segment((51,58)).segment((38,58)).arc((21,60),(5,58)).segment((-12,58)).close().assemble(),mode='s').finalize().extrude(48).union(w1.workplane(offset=119/2).moveTo(76,0).box(30,112,119))