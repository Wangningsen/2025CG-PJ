import cadquery as cq
w0=cq.Workplane('YZ',origin=(94,0,0))
w1=cq.Workplane('ZX',origin=(0,37,0))
r=w0.sketch().segment((35,69),(37,69)).segment((37,68)).arc((51,98),(35,69)).assemble().finalize().extrude(-101).union(w1.sketch().segment((-64,-46),(-64,-19)).segment((-46,-19)).arc((-98,-29),(-62,-69)).segment((-62,-81)).segment((22,-81)).segment((22,-94)).segment((61,-94)).segment((61,-45)).segment((60,-45)).segment((60,-46)).close().assemble().finalize().extrude(-96))