import cadquery as cq
w0=cq.Workplane('YZ',origin=(-100,0,0))
r=w0.sketch().segment((-85,-97),(39,-97)).segment((39,-47)).arc((35,-38),(39,-29)).segment((39,89)).segment((-85,89)).close().assemble().push([(-23,1)]).rect(34,68,mode='s').finalize().extrude(143).union(w0.workplane(offset=200/2).moveTo(0,12).cylinder(200,85))