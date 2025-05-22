import cadquery as cq
w0=cq.Workplane('YZ',origin=(68,0,0))
r=w0.sketch().segment((-38,-100),(83,-100)).segment((83,-50)).segment((91,-50)).segment((91,-7)).segment((89,-7)).arc((-43,89),(-38,-73)).close().assemble().reset().face(w0.sketch().arc((55,-63),(69,-59),(81,-50)).segment((68,-50)).arc((62,-57),(55,-63)).assemble(),mode='s').finalize().extrude(-137)