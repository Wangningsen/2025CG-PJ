import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-87))
w1=cq.Workplane('YZ',origin=(-15,0,0))
r=w0.sketch().push([(22,62)]).circle(38).circle(37,mode='s').finalize().extrude(49).union(w1.sketch().arc((-68,51),(-69,56),(-63,56)).arc((-95,81),(-68,51)).assemble().finalize().extrude(-45))