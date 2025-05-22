import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-26))
r=w0.sketch().arc((-92,-26),(-74,8),(-50,55)).arc((-93,29),(-92,-26)).assemble().reset().face(w0.sketch().arc((-45,-50),(2,-14),(-4,31)).arc((-13,13),(-25,-4)).arc((-30,-20),(-39,-35)).arc((-41,-43),(-45,-50)).assemble()).push([(90.5,-11)]).rect(19,88).push([(90,22)]).rect(8,8,mode='s').finalize().extrude(52)