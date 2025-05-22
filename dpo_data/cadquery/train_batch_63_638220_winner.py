import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-37,0))
r=w0.sketch().segment((61,-34),(70,-42)).segment((87,-23)).segment((79,-15)).close().assemble().finalize().extrude(-63).union(w0.sketch().push([(-55,10)]).circle(32).circle(13,mode='s').finalize().extrude(137))