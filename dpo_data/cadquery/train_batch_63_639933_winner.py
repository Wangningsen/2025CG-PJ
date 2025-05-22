import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,44,0))
w1=cq.Workplane('ZX',origin=(0,17,0))
r=w0.sketch().arc((44,67),(78,10),(65,76)).arc((51,77),(44,67)).assemble().finalize().extrude(-81).union(w0.sketch().segment((-100,12),(-60,-77)).segment((12,-45)).arc((59,-23),(15,5)).segment((-20,57)).close().assemble().finalize().extrude(2)).union(w1.sketch().arc((-9,-29),(35,-69),(2,-21)).segment((2,-4)).segment((-9,-4)).close().assemble().push([(21,-45)]).rect(12,32,mode='s').finalize().extrude(-63))