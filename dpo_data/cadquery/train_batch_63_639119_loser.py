import cadquery as cq
w0=cq.Workplane('YZ',origin=(7,0,0))
r=w0.sketch().rect(170,200).reset().face(w0.sketch().segment((33,-5),(45,-5)).segment((45,-2)).segment((66,-2)).segment((66,2)).segment((45,2)).segment((45,5)).segment((33,5)).close().assemble(),mode='s').finalize().extrude(-14)