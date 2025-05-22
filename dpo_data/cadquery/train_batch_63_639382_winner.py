import cadquery as cq
w0=cq.Workplane('YZ',origin=(-61,0,0))
r=w0.sketch().arc((39,95),(40,98),(39,100)).close().assemble().finalize().extrude(38).union(w0.sketch().push([(-79,-92)]).circle(8).push([(19,-20)]).circle(68).circle(36,mode='s').finalize().extrude(121))