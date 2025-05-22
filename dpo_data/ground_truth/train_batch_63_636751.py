import cadquery as cq
w0=cq.Workplane('YZ',origin=(-63,0,0))
r=w0.sketch().push([(42,-49)]).circle(51).circle(14,mode='s').finalize().extrude(126).union(w0.sketch().segment((-93,100),(-82,92)).arc((-87,97),(-93,100)).assemble().finalize().extrude(127))