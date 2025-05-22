import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,38,0))
r=w0.sketch().push([(36,46.5)]).rect(50,7).rect(38,1,mode='s').finalize().extrude(-92).union(w0.sketch().segment((-47,-50),(-47,36)).segment((-27,36)).arc((-99,8),(-47,-50)).assemble().reset().face(w0.sketch().segment((56,-27),(100,-27)).arc((78,-18),(56,-27)).assemble()).finalize().extrude(16))