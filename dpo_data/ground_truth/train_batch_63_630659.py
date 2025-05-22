import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-10))
r=w0.sketch().segment((-81,-57),(-50,-57)).segment((-22,-65)).segment((-20,-57)).segment((11,-57)).segment((11,-46)).arc((100,-20),(11,6)).segment((11,60)).segment((-20,60)).segment((-48,68)).segment((-50,60)).segment((-81,60)).close().assemble().finalize().extrude(10).union(w0.workplane(offset=21/2).moveTo(-26.5,22).box(147,40,21))