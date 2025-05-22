import cadquery as cq
w0=cq.Workplane('YZ',origin=(-100,0,0))
r=w0.sketch().segment((-62,60),(4,-72)).arc((25,-70),(34,-84)).segment((43,-65)).segment((62,-66)).segment((-13,84)).close().assemble().finalize().extrude(200)