import cadquery as cq
w0=cq.Workplane('YZ',origin=(-45,0,0))
w1=cq.Workplane('YZ',origin=(-44,0,0))
r=w0.sketch().arc((-66,-1),(-30,-100),(22,-9)).segment((86,-9)).segment((86,50)).segment((-1,50)).segment((-1,12)).arc((-17,17),(-33,18)).segment((-33,100)).segment((-56,100)).segment((-56,10)).arc((-63,5),(-66,-1)).assemble().finalize().extrude(45).union(w1.sketch().push([(-54,55)]).circle(7).circle(4,mode='s').finalize().extrude(89))