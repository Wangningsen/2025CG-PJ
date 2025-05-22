import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-2,0))
r=w0.sketch().push([(-48,-31)]).circle(52).circle(26,mode='s').finalize().extrude(-22).union(w0.sketch().segment((73,72),(100,72)).arc((87,83),(73,72)).assemble().finalize().extrude(27))