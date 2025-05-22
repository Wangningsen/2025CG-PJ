import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,33,0))
r=w0.sketch().segment((-72,60),(-18,29)).segment((6,70)).segment((-49,100)).close().assemble().reset().face(w0.sketch().arc((34,-27),(0,-93),(59,-56)).arc((65,-22),(34,-27)).assemble()).finalize().extrude(-66)