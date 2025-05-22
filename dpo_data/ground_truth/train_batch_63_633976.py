import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.sketch().segment((-62,60),(4,-72)).arc((23,-69),(34,-84)).segment((36,-83)).segment((43,-65)).segment((56,-70)).segment((59,-64)).segment((62,-66)).segment((-13,84)).close().assemble().finalize().extrude(-200)