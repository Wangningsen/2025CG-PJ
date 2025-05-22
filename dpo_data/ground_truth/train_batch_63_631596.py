import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-28,0))
r=w0.sketch().arc((-85,-60),(-85,-56),(-81,-58)).arc((-94,-38),(-85,-60)).assemble().reset().face(w0.sketch().arc((38,36),(70,-32),(70,43)).arc((49,60),(38,36)).assemble()).finalize().extrude(55)