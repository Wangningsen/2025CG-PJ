import cadquery as cq
w0=cq.Workplane('YZ',origin=(46,0,0))
w1=cq.Workplane('XY',origin=(0,0,-66))
r=w0.sketch().segment((-66,-87),(-43,-87)).segment((-43,-56)).segment((46,-56)).segment((46,48)).segment((-54,48)).segment((-54,-35)).segment((-66,-35)).close().assemble().finalize().extrude(-7).union(w1.sketch().segment((-88,34),(17,34)).arc((-22,-3),(-3,-54)).arc((59,-97),(75,-23)).arc((67,14),(36,34)).segment((68,34)).segment((68,100)).segment((-88,100)).close().assemble().finalize().extrude(153))