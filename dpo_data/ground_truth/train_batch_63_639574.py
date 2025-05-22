import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-1,0))
r=w0.sketch().push([(-48,-31)]).circle(52).circle(26,mode='s').finalize().extrude(-23).union(w0.sketch().segment((73,72),(100,72)).arc((86,83),(73,72)).assemble().finalize().extrude(26))