import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,33,0))
r=w0.sketch().segment((-72,60),(-17,29)).segment((6,69)).segment((-49,100)).close().assemble().reset().face(w0.sketch().arc((34,-27),(-7,-86),(59,-56)).arc((67,-24),(34,-27)).assemble()).finalize().extrude(-66)