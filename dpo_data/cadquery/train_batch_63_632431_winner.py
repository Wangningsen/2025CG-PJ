import cadquery as cq
w0=cq.Workplane('YZ',origin=(69,0,0))
r=w0.sketch().segment((-38,-100),(83,-100)).segment((83,-55)).arc((89,-51),(91,-45)).segment((91,-10)).arc((-41,90),(-38,-73)).close().assemble().reset().face(w0.sketch().segment((55,-63),(81,-53)).segment((80,-50)).segment((55,-60)).close().assemble(),mode='s').finalize().extrude(-138)